"""
Graphify

Decision Evidence Collector

Read-only evidence collector for engineering decisions.

Responsibilities:
- collect local repository evidence
- collect optional externally supplied evidence
- classify evidence as DIRECT / RELATED / CONTEXT
- preserve external integration state
- provide canonical evidence counts and provenance

This component does NOT:
- create decisions
- create plans
- execute work
- mutate repositories
- infer causality
- infer outcomes
- authenticate external providers
- fetch external APIs directly

External provider fetching/authentication remains outside this collector.
"""

from __future__ import annotations

import os
import subprocess
from pathlib import Path
from typing import Any


class DecisionEvidenceCollector:
    """
    Collects evidence relevant to an engineering decision.

    External evidence is supplied by provider adapters such as
    GitHubEvidenceAdapter. The collector only normalizes and integrates
    that evidence into the canonical evidence stream.
    """

    VERSION = "38.5"

    # --------------------------------------------------
    # Evidence classifications
    # --------------------------------------------------

    DIRECT = "DIRECT"
    RELATED = "RELATED"
    CONTEXT = "CONTEXT"

    # --------------------------------------------------
    # External integration states
    # --------------------------------------------------

    NOT_REQUESTED = "NOT_REQUESTED"

    UNKNOWN = "UNKNOWN"

    # --------------------------------------------------
    # Excluded repository paths
    # --------------------------------------------------

    DEFAULT_EXCLUDED_DIRECTORIES = {
        ".git",
        ".graphify",
        ".pytest_cache",
        ".venv",
        "__pycache__",
        "build",
        "dist",
        "node_modules",
        "venv",
    }

    GENERATED_MARKERS = {
        ".graphify_stage_",
        ".graphify-fixture-",
        "graphify_stage_",
    }

    GENERATED_NAMES = {
        "graphify-out",
        "graphify_export",
        "graphify_exports",
    }

    # --------------------------------------------------
    # Public API
    # --------------------------------------------------

    def collect(
        self,
        repository_path: str | os.PathLike[str],
        decision: Any,
        repository_plan: Any | None = None,
        external_evidence: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """
        Collect canonical decision evidence.

        Parameters
        ----------
        repository_path:
            Repository to inspect.

        decision:
            Canonical engineering decision or decision-like mapping.

        repository_plan:
            Optional repository plan used only as additional context.

        external_evidence:
            Optional provider-produced evidence payload.

            Example:

            {
                "source": "github",
                "status": "CONNECTED_NO_EVIDENCE",
                "connected": True,
                "evidence_available": False,
                "evidence_count": 0,
                "evidence": [],
                "counts": {
                    "pull_requests": 0,
                    "commits": 0,
                    "checks": 0,
                },
            }

        Returns
        -------
        dict
            Canonical evidence collection containing local evidence,
            external evidence, integration state, counts, and provenance.

        Important:
            Integration state is intentionally independent from the
            presence/absence of evidence items.

            Therefore:

                connected + 0 evidence
                    !=
                not requested

            and:

                connected + 0 evidence
                    !=
                integration failure
        """

        repository = Path(repository_path).resolve()

        decision_terms = self._decision_terms(
            decision=decision,
            repository_plan=repository_plan,
        )

        # --------------------------------------------------
        # Local evidence
        # --------------------------------------------------

        direct: list[dict[str, Any]] = []
        related: list[dict[str, Any]] = []
        context: list[dict[str, Any]] = []

        # --------------------------------------------------
        # Git evidence
        # --------------------------------------------------

        commits = self._git_commits(repository)

        for commit in commits:
            evidence = self._classify_local_evidence(
                evidence={
                    "type": "git_commit",
                    "id": commit,
                    "value": commit,
                    "path": None,
                    "source": "git",
                },
                decision_terms=decision_terms,
            )

            self._append_classified(
                evidence=evidence,
                direct=direct,
                related=related,
                context=context,
            )

        diff = self._git_diff(repository)

        if diff:
            evidence = self._classify_local_evidence(
                evidence={
                    "type": "git_diff",
                    "id": "current-diff",
                    "value": diff,
                    "path": None,
                    "source": "git",
                },
                decision_terms=decision_terms,
            )

            self._append_classified(
                evidence=evidence,
                direct=direct,
                related=related,
                context=context,
            )

        # --------------------------------------------------
        # Repository documents / files
        # --------------------------------------------------

        documents = self._documents(repository)

        for path in documents:
            evidence = self._document_evidence(
                path=path,
                repository=repository,
                decision_terms=decision_terms,
            )

            if evidence is None:
                continue

            self._append_classified(
                evidence=evidence,
                direct=direct,
                related=related,
                context=context,
            )

        repository_files = self._repository_files(repository)

        for path in repository_files:
            evidence = self._repository_file_evidence(
                path=path,
                repository=repository,
                decision_terms=decision_terms,
            )

            if evidence is None:
                continue

            self._append_classified(
                evidence=evidence,
                direct=direct,
                related=related,
                context=context,
            )

        # --------------------------------------------------
        # External evidence
        # --------------------------------------------------

        external = self._normalize_external_evidence(
            external_evidence=external_evidence,
            decision_terms=decision_terms,
        )

        # --------------------------------------------------
        # External integration state
        #
        # IMPORTANT:
        # This is intentionally NOT derived from bool(external).
        # A provider can be connected and legitimately return zero
        # evidence.
        # --------------------------------------------------

        external_integration = (
            self._external_integration_state(
                external_evidence=external_evidence,
                normalized_external=external,
            )
        )

        # --------------------------------------------------
        # Counts
        # --------------------------------------------------

        counts = {
            "direct": len(direct),
            "related": len(related),
            "context": len(context),
            "external": len(external),
        }

        counts["total"] = (
            counts["direct"]
            + counts["related"]
            + counts["context"]
            + counts["external"]
        )

        # --------------------------------------------------
        # Provenance
        # --------------------------------------------------

        external_providers = list(
            external_integration.get(
                "providers",
                [],
            )
        )

        external_statuses = self._external_statuses(
            external_evidence=external_evidence,
            normalized_external=external,
        )

        provenance = {
            "version": self.VERSION,
            "read_only": True,
            "creates_decision": False,
            "creates_plan": False,
            "executes_work": False,
            "mutates_repository": False,
            "infers_causality": False,
            "causality_status": "NOT_INFERRED",
            "external_evidence": bool(external),
            "external_providers": external_providers,
            "external_statuses": external_statuses,
            "external_integration": external_integration,
        }

        return {
            "repository": str(repository),
            "evidence": {
                "direct": direct,
                "related": related,
                "context": context,
                "external": external,
            },
            "counts": counts,
            "external_counts": {
                "total": len(external),
            },
            "external_integration": external_integration,
            "provenance": provenance,
            "version": self.VERSION,
        }

    # ==================================================
    # External Integration
    # ==================================================

    def _external_integration_state(
        self,
        external_evidence: dict[str, Any] | None,
        normalized_external: list[dict[str, Any]],
    ) -> dict[str, Any]:
        """
        Normalize provider integration state.

        This is the canonical distinction between:

        NOT_REQUESTED
        CONNECTED_WITH_EVIDENCE
        CONNECTED_NO_EVIDENCE
        AUTHENTICATION_FAILED
        PERMISSION_DENIED
        RATE_LIMITED
        NETWORK_ERROR
        REPOSITORY_UNAVAILABLE
        INVALID_REPOSITORY
        UNKNOWN

        Evidence count is deliberately independent from status.
        """

        # No provider was requested.
        if external_evidence is None:
            return {
                "requested": False,
                "connected": False,
                "status": self.NOT_REQUESTED,
                "providers": [],
                "evidence_count": 0,
            }

        provider = (
            external_evidence.get("source")
            or external_evidence.get("provider")
        )

        providers: list[str] = []

        if provider:
            providers.append(str(provider))

        # Preserve explicitly supplied provider collections.
        supplied_providers = external_evidence.get(
            "providers"
        )

        if isinstance(supplied_providers, (list, tuple, set)):
            for item in supplied_providers:
                if item is None:
                    continue

                value = str(item)

                if value and value not in providers:
                    providers.append(value)

        status = external_evidence.get(
            "status",
            self.UNKNOWN,
        )

        if not status:
            status = self.UNKNOWN

        connected = bool(
            external_evidence.get(
                "connected",
                False,
            )
        )

        # Prefer provider-reported evidence count because it is the
        # canonical count from the external source. Fall back to the
        # normalized evidence stream when unavailable.
        evidence_count = external_evidence.get(
            "evidence_count"
        )

        if evidence_count is None:
            evidence_count = len(
                normalized_external
            )

        try:
            evidence_count = max(
                0,
                int(evidence_count),
            )
        except (
            TypeError,
            ValueError,
        ):
            evidence_count = len(
                normalized_external
            )

        return {
            "requested": True,
            "connected": connected,
            "status": str(status),
            "providers": providers,
            "evidence_count": evidence_count,
        }

    def _external_statuses(
        self,
        external_evidence: dict[str, Any] | None,
        normalized_external: list[dict[str, Any]],
    ) -> list[str]:
        """
        Return unique externally observed integration statuses.
        """

        statuses: list[str] = []

        if external_evidence is not None:
            status = external_evidence.get("status")

            if status:
                value = str(status)

                if value not in statuses:
                    statuses.append(value)

        for item in normalized_external:

            status = item.get(
                "external_status"
            )

            if not status:
                continue

            value = str(status)

            if value not in statuses:
                statuses.append(value)

        return statuses

    # ==================================================
    # External Evidence Normalization
    # ==================================================

    def _normalize_external_evidence(
        self,
        external_evidence: dict[str, Any] | None,
        decision_terms: set[str],
    ) -> list[dict[str, Any]]:
        """
        Normalize externally supplied evidence into the canonical
        evidence stream.

        The collector does not authenticate, fetch, rank, or infer
        causality for external evidence.
        """

        if not external_evidence:
            return []

        raw_evidence = external_evidence.get(
            "evidence",
            [],
        )

        if not isinstance(
            raw_evidence,
            list,
        ):
            return []

        provider = (
            external_evidence.get("source")
            or external_evidence.get("provider")
            or "external"
        )

        provider_status = (
            external_evidence.get(
                "status"
            )
            or self.UNKNOWN
        )

        normalized: list[dict[str, Any]] = []

        for item in raw_evidence:

            if not isinstance(
                item,
                dict,
            ):
                continue

            evidence = dict(item)

            evidence.setdefault(
                "evidence_source",
                "external",
            )

            evidence.setdefault(
                "external_provider",
                provider,
            )

            evidence.setdefault(
                "external_status",
                provider_status,
            )

            evidence.setdefault(
                "causality_status",
                "NOT_INFERRED",
            )

            evidence.setdefault(
                "classification",
                self.CONTEXT,
            )

            evidence.setdefault(
                "evidence_strength",
                "CONTEXT",
            )

            # External provider evidence is observational.
            evidence[
                "causality_status"
            ] = "NOT_INFERRED"

            # Give evidence a canonical text representation only when
            # the provider did not already provide one.
            if not evidence.get("text"):
                evidence["text"] = self._external_text(
                    evidence
                )

            # External evidence can be classified against decision
            # terms, but the collector does not infer causality.
            classification = (
                self._external_classification(
                    evidence=evidence,
                    decision_terms=decision_terms,
                )
            )

            evidence[
                "classification"
            ] = classification

            normalized.append(
                evidence
            )

        return normalized

    @staticmethod
    def _external_text(
        evidence: dict[str, Any],
    ) -> str:
        """
        Build a stable searchable representation for external evidence.
        """

        fields = (
            "title",
            "message",
            "name",
            "check_name",
            "repository",
            "pull_request",
            "commit",
        )

        values: list[str] = []

        for field in fields:
            value = evidence.get(field)

            if value is None:
                continue

            text = str(value).strip()

            if text:
                values.append(text)

        return " ".join(values)

    def _external_classification(
        self,
        evidence: dict[str, Any],
        decision_terms: set[str],
    ) -> str:
        """
        Classify external evidence by relevance.

        This classification is evidence relevance only.
        It is not causal attribution.
        """

        existing_classification = evidence.get(
            "classification"
        )

        if existing_classification in {
            self.DIRECT,
            self.RELATED,
            self.CONTEXT,
        }:
            # Preserve explicit provider classification where present.
            if existing_classification == "VERIFICATION":
                return self.DIRECT

            return str(
                existing_classification
            )

        text = str(
            evidence.get("text", "")
        ).lower()

        if not text:
            return self.CONTEXT

        if decision_terms.intersection(
            self._tokens(text)
        ):
            return self.DIRECT

        return self.RELATED

    # ==================================================
    # Decision Terms
    # ==================================================

    def _decision_terms(
        self,
        decision: Any,
        repository_plan: Any | None = None,
    ) -> set[str]:
        """
        Extract searchable decision/plan terms.
        """

        terms: set[str] = set()

        self._collect_terms(
            decision,
            terms,
        )

        self._collect_terms(
            repository_plan,
            terms,
        )

        return terms

    def _collect_terms(
        self,
        value: Any,
        terms: set[str],
    ) -> None:

        if value is None:
            return

        if isinstance(
            value,
            dict,
        ):

            preferred_keys = (
                "decision",
                "selected_goal",
                "goal",
                "strategy",
                "strategic_focus",
                "objective",
                "plan_objective",
                "expected_result",
                "expected_outcome",
                "rationale",
                "summary",
                "description",
            )

            for key in preferred_keys:

                if key not in value:
                    continue

                self._collect_terms(
                    value.get(key),
                    terms,
                )

            return

        if isinstance(
            value,
            (list, tuple, set),
        ):

            for item in value:
                self._collect_terms(
                    item,
                    terms,
                )

            return

        tokens = self._tokens(
            str(value)
        )

        terms.update(tokens)

    @staticmethod
    def _tokens(
        text: str,
    ) -> set[str]:

        return {
            token
            for token in (
                text.lower()
                .replace("_", " ")
                .replace("-", " ")
                .split()
            )
            if len(token) > 2
        }

    # ==================================================
    # Local Evidence Classification
    # ==================================================

    def _classify_local_evidence(
        self,
        evidence: dict[str, Any],
        decision_terms: set[str],
    ) -> dict[str, Any]:
        """
        Classify local evidence.

        Classification:
        - DIRECT when decision terms occur in the evidence
        - RELATED when evidence is weakly connected
        - CONTEXT otherwise
        """

        value = str(
            evidence.get(
                "value",
                "",
            )
        )

        tokens = self._tokens(value)

        if decision_terms.intersection(tokens):
            classification = self.DIRECT

        elif evidence.get("type") in {
            "git_commit",
            "git_diff",
        }:
            classification = self.RELATED

        else:
            classification = self.CONTEXT

        result = dict(evidence)

        result[
            "classification"
        ] = classification

        result.setdefault(
            "evidence_source",
            "local",
        )

        result.setdefault(
            "causality_status",
            "NOT_INFERRED",
        )

        return result

    @staticmethod
    def _append_classified(
        evidence: dict[str, Any],
        direct: list[dict[str, Any]],
        related: list[dict[str, Any]],
        context: list[dict[str, Any]],
    ) -> None:

        classification = evidence.get(
            "classification"
        )

        if classification == DecisionEvidenceCollector.DIRECT:
            direct.append(evidence)

        elif classification == DecisionEvidenceCollector.RELATED:
            related.append(evidence)

        else:
            context.append(evidence)

    # ==================================================
    # Documents
    # ==================================================

    def _documents(
        self,
        repository: Path,
    ) -> list[Path]:
        """
        Discover high-value engineering documents.
        """

        documents: list[Path] = []

        if not repository.exists():
            return documents

        for path in repository.rglob("*"):

            if not path.is_file():
                continue

            if self._excluded(
                path,
                repository,
            ):
                continue

            name = path.name.lower()

            if (
                name == "readme.md"
                or "architecture" in name
                or "design" in name
                or "decision" in name
                or "decisions" in name
                or "adr" in name
            ):
                documents.append(path)

        return documents

    def _document_evidence(
        self,
        path: Path,
        repository: Path,
        decision_terms: set[str],
    ) -> dict[str, Any] | None:
        """
        Build evidence from an engineering document.
        """

        try:

            text = path.read_text(
                encoding="utf-8",
                errors="ignore",
            )

        except OSError:

            return None

        if not text.strip():
            return None

        relative_path = self._relative_path(
            path,
            repository,
        )

        evidence = {
            "type": "repository_document",
            "path": relative_path,
            "value": text[:12000],
            "excerpt": self._excerpt(text),
            "source": "repository",
        }

        return self._classify_local_evidence(
            evidence=evidence,
            decision_terms=decision_terms,
        )

    # ==================================================
    # Repository Files
    # ==================================================

    def _repository_files(
        self,
        repository: Path,
    ) -> list[Path]:
        """
        Discover relevant repository implementation files.

        This intentionally remains conservative to avoid flooding the
        evidence stream with generated or unrelated files.
        """

        files: list[Path] = []

        if not repository.exists():
            return files

        allowed_suffixes = {
            ".py",
            ".js",
            ".ts",
            ".tsx",
            ".jsx",
            ".java",
            ".cpp",
            ".c",
            ".h",
            ".hpp",
            ".go",
            ".rs",
            ".cs",
        }

        for path in repository.rglob("*"):

            if not path.is_file():
                continue

            if self._excluded(
                path,
                repository,
            ):
                continue

            if path.suffix.lower() not in allowed_suffixes:
                continue

            files.append(path)

        return files

    def _repository_file_evidence(
        self,
        path: Path,
        repository: Path,
        decision_terms: set[str],
    ) -> dict[str, Any] | None:
        """
        Build evidence from an implementation file.
        """

        try:

            text = path.read_text(
                encoding="utf-8",
                errors="ignore",
            )

        except OSError:

            return None

        if not text.strip():
            return None

        relative_path = self._relative_path(
            path,
            repository,
        )

        evidence = {
            "type": "repository_file",
            "path": relative_path,
            "value": text[:12000],
            "excerpt": self._excerpt(text),
            "source": "repository",
        }

        return self._classify_local_evidence(
            evidence=evidence,
            decision_terms=decision_terms,
        )

    # ==================================================
    # Git
    # ==================================================

    @staticmethod
    def _git_commits(
        repository: Path,
        limit: int = 20,
    ) -> list[str]:

        try:

            output = subprocess.check_output(
                [
                    "git",
                    "-C",
                    str(repository),
                    "log",
                    "--oneline",
                    f"-{limit}",
                ],
                text=True,
                stderr=subprocess.DEVNULL,
            )

        except Exception:

            return []

        return [
            line.strip()
            for line in output.splitlines()
            if line.strip()
        ]

    @staticmethod
    def _git_diff(
        repository: Path,
    ) -> str:

        try:

            output = subprocess.check_output(
                [
                    "git",
                    "-C",
                    str(repository),
                    "diff",
                ],
                text=True,
                stderr=subprocess.DEVNULL,
            )

        except Exception:

            return ""

        return output.strip()

    # ==================================================
    # Helpers
    # ==================================================

    def _excluded(
        self,
        path: Path,
        repository: Path,
    ) -> bool:

        try:
            relative = path.relative_to(
                repository
            )
        except ValueError:
            return True

        parts = relative.parts

        for part in parts:

            lower = part.lower()

            if lower in self.DEFAULT_EXCLUDED_DIRECTORIES:
                return True

            for marker in self.GENERATED_MARKERS:

                if marker.lower() in lower:
                    return True

            for name in self.GENERATED_NAMES:

                if lower == name.lower():
                    return True

        return False

    @staticmethod
    def _relative_path(
        path: Path,
        repository: Path,
    ) -> str:

        try:
            return str(
                path.relative_to(repository)
            )
        except ValueError:
            return str(path)

    @staticmethod
    def _excerpt(
        text: str,
        limit: int = 600,
    ) -> str:

        normalized = " ".join(
            text.split()
        )

        if len(normalized) <= limit:
            return normalized

        return normalized[:limit] + "..."