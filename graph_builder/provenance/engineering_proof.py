"""
Graphify

Phase 39
Stage 39.1

Canonical Engineering Proof

EngineeringProof is a read-only customer-facing projection over the
existing canonical engineering provenance.

It does NOT:
- create decisions
- create plans
- create evidence
- execute work
- infer causality
- infer outcomes
- mutate repositories
- become a new source of truth

Canonical ownership remains upstream:

Decision
    -> RepositoryDecisionEngine

Plan
    -> RepositoryExecutionPlanningEngine

Evidence
    -> DecisionEvidenceCollector / canonical evidence layer

Execution
    -> EngineeringKernel / canonical execution layer

Outcome
    -> EngineeringInsightResult / canonical outcome layer
"""

from __future__ import annotations

from typing import Any


class EngineeringProof:

    VERSION = "39.1"

    STATUS = "READ_ONLY_PROOF"

    UNKNOWN = "UNKNOWN"

    # ==================================================
    # Public API
    # ==================================================

    def build(
        self,
        record: dict[str, Any],
        review: dict[str, Any] | None = None,
    ) -> dict[str, Any]:

        if not isinstance(record, dict):
            raise TypeError(
                "record must be a dictionary."
            )

        if review is not None and not isinstance(review, dict):
            raise TypeError(
                "review must be a dictionary or None."
            )

        decision = (
            record.get(
                "decision",
                {},
            )
            or {}
        )

        plan = (
            record.get(
                "plan",
                {},
            )
            or {}
        )

        evidence = (
            record.get(
                "evidence",
                {},
            )
            or {}
        )

        knowledge = (
            record.get(
                "knowledge",
                {},
            )
            or {}
        )

        provenance = (
            record.get(
                "provenance",
                {},
            )
            or {}
        )

        review = review or {}

        execution = (
            review.get(
                "execution",
                {},
            )
            or {}
        )

        external_integration = (
            review.get(
                "external_integration",
            )
            or provenance.get(
                "external_integration",
            )
            or knowledge.get(
                "external_integration",
            )
            or self._default_external_integration()
        )

        selected_evidence = (
            review.get(
                "evidence",
                [],
            )
            or []
        )

        if not selected_evidence:
            selected_evidence = self._flatten_evidence(
                evidence
            )

        # --------------------------------------------------
        # Presentation-safe evidence projection
        # --------------------------------------------------
        # EngineeringProof must never expose the raw
        # evidence "value" payload. Keep only the metadata
        # and compact excerpt needed by the customer-facing
        # proof.
        selected_evidence = [
            normalized
            for item in selected_evidence
            for normalized in [
                self._proof_evidence_item(item)
            ]
            if normalized is not None
        ]

        # --------------------------------------------------
        # Semantic evidence scopes
        # --------------------------------------------------
        #
        # Selected evidence may contain different semantic
        # roles. A verification artifact must not be
        # presented as evidence explaining WHY a decision
        # was made.
        #

        why_evidence = [
            item
            for item in selected_evidence
            if item.get("role")
            in {
                "DECISION",
                "ARCHITECTURE",
                "RISK",
                "DOCUMENTATION",
            }
        ]

        verification_evidence = [
            item
            for item in selected_evidence
            if item.get("role")
            == "VERIFICATION"
        ]

        decision_projection = self._decision(
            decision
        )

        change = self._change(
            evidence=evidence,
            review=review,
        )

        verification = self._verification(
            evidence=evidence,
            review=review,
            selected_evidence=verification_evidence,
        )

        outcome = self._outcome(
            execution=execution,
            review=review,
        )

        unknowns = self._unknowns(
            decision=decision,
            plan=plan,
            evidence=evidence,
            execution=execution,
            outcome=outcome,
            provenance=provenance,
        )

        trust = self._trust(
            decision=decision,
            provenance=provenance,
            execution=execution,
            outcome=outcome,
        )

        timeline = self._timeline(
            evidence=evidence,
            execution=execution,
        )

        status = self._proof_status(
            execution=execution,
            verification=verification,
            outcome=outcome,
        )

        external_binding = self._external_binding(
            record=record,
            review=review,
        )

        return {
            "proof_version": self.VERSION,

            "status": status,

            "proof_type": (
                "Engineering Proof"
            ),

            "repository": record.get(
                "repository",
                self.UNKNOWN,
            ),

            "repository_path": record.get(
                "repository_path",
                self.UNKNOWN,
            ),

            "decision": decision_projection,

            "why": {
                "evidence": why_evidence,

                "summary": self._decision_summary(
                    decision=decision,
                    evidence_count=len(
                        why_evidence
                    ),
                ),
            },

            "change": change,

            "verification": verification,

            "outcome": outcome,

            "external_integration": (
                self._normalize_external_integration(
                    external_integration
                )
            ),

            "external_binding":
                external_binding,

            "timeline": timeline,

            "unknowns": unknowns,

            "trust": trust,

            "provenance": {
                "source":
                    "EngineeringDecisionRecord",

                "review_source":
                    "EngineeringReview",

                "read_only":
                    True,

                "creates_decision":
                    False,

                "creates_plan":
                    False,

                "creates_evidence":
                    False,

                "executes_work":
                    False,

                "mutates_repository":
                    False,

                "infers_causality":
                    False,

                "infers_outcome":
                    False,
            },
        }

    # ==================================================
    # Decision
    # ==================================================

    @staticmethod
    def _decision(
        decision: dict[str, Any],
    ) -> dict[str, Any]:

        return {
            "statement":
                decision.get(
                    "decision",
                    decision.get(
                        "selected_decision",
                        "UNKNOWN",
                    ),
                ),

            "goal":
                decision.get(
                    "selected_goal",
                    "UNKNOWN",
                ),

            "strategy":
                decision.get(
                    "strategy",
                    decision.get(
                        "strategic_focus",
                        "UNKNOWN",
                    ),
                ),

            "priority":
                decision.get(
                    "priority",
                    "UNKNOWN",
                ),
        }

    # ==================================================
    # Presentation-safe decision summary
    # ==================================================

    @staticmethod
    def _decision_summary(
        decision: dict[str, Any],
        evidence_count: int,
    ) -> str:

        statement = (
            decision.get(
                "decision",
                "UNKNOWN",
            )
            or "UNKNOWN"
        )

        goal = (
            decision.get(
                "selected_goal",
                "UNKNOWN",
            )
            or "UNKNOWN"
        )

        reason = (
            decision.get("decision_reason", "UNKNOWN") or "UNKNOWN"
        ).strip().rstrip(".")

        priority = (
            decision.get(
                "priority",
                "UNKNOWN",
            )
            or "UNKNOWN"
        )

        confidence = (
            decision.get(
                "confidence",
                "UNKNOWN",
            )
            or "UNKNOWN"
        )

        summary = (
            f"Decision: {statement}. "
            f"Goal: {goal}. "
            f"Rationale: {reason}. "
            f"Priority: {priority}. "
            f"Confidence: {confidence}."
        )

        if evidence_count > 0:
            summary += (
                " Supporting decision evidence items: "
                f"{evidence_count}."
            )
        else:
            summary += (
                " No decision-supporting evidence was selected."
            )

        return summary

    # ==================================================
    # Change
    # ==================================================

    @staticmethod
    def _change(
        evidence: dict[str, Any],
        review: dict[str, Any],
    ) -> dict[str, Any]:

        external = (
            evidence.get(
                "external",
                [],
            )
            or []
        )

        if not isinstance(external, list):
            external = []

        pull_requests = [
            item
            for item in external
            if isinstance(item, dict)
            and item.get("type")
            == "github_pull_request"
        ]

        commits = [
            item
            for item in external
            if isinstance(item, dict)
            and item.get("type")
            == "github_commit"
        ]

        files = [
            item
            for item in external
            if isinstance(item, dict)
            and item.get("type")
            == "github_file"
        ]

        files_changed = [
            item.get("path")
            for item in files
            if item.get("path")
        ]

        for path_value in EngineeringProof._collect_changed_files(
            commits
        ):
            if path_value not in files_changed:
                files_changed.append(path_value)

        return {
            "pull_requests":
                pull_requests,

            "commits":
                commits,

            "files_changed":
                files_changed,

            "status":
                (
                    "OBSERVED"
                    if pull_requests or commits
                    else "UNKNOWN"
                ),
        }

    # ==================================================
    # Verification
    # ==================================================

    @staticmethod
    def _verification(
        evidence: dict[str, Any],
        review: dict[str, Any],
        selected_evidence: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:

        external = (
            evidence.get(
                "external",
                [],
            )
            or []
        )

        if not isinstance(external, list):
            external = []

        selected_evidence = (
            selected_evidence
            if isinstance(
                selected_evidence,
                list,
            )
            else []
        )
        verification_evidence = [
            {
                "type": item.get("type"),
                "path": item.get("path"),
                "relevance": item.get("relevance"),
                "strength": item.get("strength"),
                "score": item.get("score"),
                "role": item.get("role"),
            }
            for item in selected_evidence
            if isinstance(item, dict)
        ]

        checks = [
            item
            for item in external
            if isinstance(item, dict)
            and item.get("type")
            == "github_check"
        ]

        review_projection = (
            review.get(
                "execution",
                {},
            )
            or {}
        )

        validation = review_projection.get(
            "validation",
            "NOT_AVAILABLE",
        )

        review_status = review_projection.get(
            "review",
            "NOT_AVAILABLE",
        )
        for check in checks:
            if (
                isinstance(check, dict)
                and check.get("type") == "github_check"
            ):
                check["classification"] = "VERIFICATION"
        return {
            "evidence":
                verification_evidence,

            "checks":
                checks,

            "validation":
                validation,

            "review":
                review_status,

            "status":
                EngineeringProof._verification_status(
                    checks=checks,
                    validation=validation,
                    review_status=review_status,
                ),
        }

    @staticmethod
    def _verification_status(
        checks: list[dict[str, Any]],
        validation: str,
        review_status: str,
    ) -> str:

        if validation == "VERIFIED":
            return "VERIFIED"

        successful_checks = [
            check
            for check in checks
            if check.get("conclusion")
            == "success"
        ]

        if (
            successful_checks
            and review_status == "COMPLETED"
        ):
            return "VERIFIED"

        if checks or validation not in {
            "NOT_AVAILABLE",
            "UNKNOWN",
        }:
            return "PARTIAL"

        return "UNKNOWN"

    # ==================================================
    # Outcome
    # ==================================================

    @staticmethod
    def _outcome(
        execution: dict[str, Any],
        review: dict[str, Any],
    ) -> dict[str, Any]:

        value = (
            execution.get(
                "outcome",
            )
            or review.get(
                "outcome",
            )
            or "UNKNOWN"
        )

        validation = execution.get(
            "validation",
            "UNKNOWN",
        )

        review_status = execution.get(
            "review",
            "UNKNOWN",
        )

        return {
            "status":
                value,

            "validation":
                validation,

            "review":
                review_status,

            "causality":
                "UNKNOWN",
        }

    # ==================================================
    # Unknowns
    # ==================================================

    @staticmethod
    def _unknowns(
        decision,
        plan,
        evidence,
        execution,
        outcome,
        provenance,
    ) -> list[str]:

        unknowns: list[str] = []

        if not decision.get(
            "decision"
        ) and not decision.get(
            "selected_decision"
        ):
            unknowns.append(
                "Decision statement is unavailable."
            )

        if not plan:
            unknowns.append(
                "Engineering plan is unavailable."
            )

        if not evidence:
            unknowns.append(
                "Supporting evidence is unavailable."
            )

        if execution.get(
            "performed"
        ) is not True:
            unknowns.append(
                "No verified execution is recorded."
            )

        if outcome.get(
            "status"
        ) in {
            "UNKNOWN",
            "NOT_EXECUTED",
        }:
            unknowns.append(
                "No verified engineering outcome is available."
            )

        if not provenance.get(
            "causality_inference",
            False,
        ):
            unknowns.append(
                "Causal attribution remains UNKNOWN."
            )

        return list(
            dict.fromkeys(
                unknowns
            )
        )

    # ==================================================
    # Trust
    # ==================================================

    @staticmethod
    def _trust(
        decision,
        provenance,
        execution,
        outcome,
    ) -> dict[str, Any]:

        return {
            "decision_observed":
                bool(
                    isinstance(
                        decision,
                        dict,
                    )
                    and decision.get(
                        "decision",
                        "UNKNOWN",
                    )
                    not in {
                        None,
                        "",
                        "UNKNOWN",
                    }
                ),

            "work_executed":
                bool(
                    execution.get(
                        "performed",
                        False,
                    )
                ),

            "repository_mutated":
                bool(
                    provenance.get(
                        "mutates_repository",
                        False,
                    )
                ),

            "causality_inferred":
                bool(
                    provenance.get(
                        "causality_inference",
                        False,
                    )
                ),

            "outcome_verified":
                outcome.get(
                    "status"
                ) == "SUCCESSFUL",

            "read_only":
                True,
        }

    # ==================================================
    # Timeline
    # ==================================================

    @staticmethod
    def _timeline(
        evidence,
        execution,
    ) -> list[dict[str, Any]]:

        events: list[dict[str, Any]] = []

        for category in (
            "direct",
            "related",
            "context",
            "external",
        ):

            items = (
                evidence.get(
                    category,
                    [],
                )
                or []
            )

            if not isinstance(items, list):
                continue

            for item in items:

                if not isinstance(item, dict):
                    continue

                timestamp = (
                    item.get("timestamp")
                    or item.get("created_at")
                    or item.get("updated_at")
                    or item.get("completed_at")
                )

                if timestamp:

                    events.append(
                        {
                            "timestamp":
                                timestamp,

                            "source":
                                item.get(
                                    "source",
                                    "UNKNOWN",
                                ),

                            "type":
                                item.get(
                                    "type",
                                    "UNKNOWN",
                                ),
                        }
                    )

        completed_at = execution.get(
            "completed_at"
        )

        if completed_at:

            events.append(
                {
                    "timestamp":
                        completed_at,

                    "source":
                        "Graphify",

                    "type":
                        "engineering_execution",
                }
            )

        return sorted(
            events,
            key=lambda item:
                str(
                    item.get(
                        "timestamp",
                        "",
                    )
                ),
        )

    # ==================================================
    # Helpers
    # ==================================================

    @staticmethod
    def _flatten_evidence(
        evidence,
    ) -> list[dict[str, Any]]:

        if not isinstance(
            evidence,
            dict,
        ):
            return []

        items: list[dict[str, Any]] = []

        for category in (
            "direct",
            "related",
            "context",
            "external",
        ):

            values = (
                evidence.get(
                    category,
                    [],
                )
                or []
            )

            if not isinstance(
                values,
                list,
            ):
                continue

            items.extend(
                item
                for item in values
                if isinstance(
                    item,
                    dict,
                )
            )

        return items

    @staticmethod
    def _collect_changed_files(
        commits,
    ) -> list[str]:

        files: list[str] = []

        for commit in commits:

            values = (
                commit.get(
                    "files",
                    [],
                )
                or []
            )

            if not isinstance(
                values,
                list,
            ):
                continue

            for value in values:

                if value and value not in files:

                    files.append(
                        str(value)
                    )

        return files

    @staticmethod
    def _external_binding(
        record,
        review,
    ):
        candidates = []

        if isinstance(review, dict):
            candidate = review.get("external_binding")
            if isinstance(candidate, dict):
                candidates.append(candidate)

        if isinstance(record, dict):
            candidate = record.get("external_binding")
            if isinstance(candidate, dict):
                candidates.append(candidate)

            provenance = record.get("provenance", {})
            if isinstance(provenance, dict):
                candidate = provenance.get("external_binding")
                if isinstance(candidate, dict):
                    candidates.append(candidate)

        for candidate in candidates:
            provider = candidate.get("provider")
            repository = candidate.get("repository")
            pull_request = candidate.get("pull_request")

            if provider and repository and pull_request is not None:
                try:
                    pull_request = int(pull_request)
                except (TypeError, ValueError):
                    continue

                return {
                    "provider": str(provider),
                    "repository": str(repository),
                    "pull_request": pull_request,
                    "binding_type": str(
                        candidate.get(
                            "binding_type",
                            "EXPLICIT",
                        )
                    ),
                    "binding_status": str(
                        candidate.get(
                            "binding_status",
                            "UNKNOWN",
                        )
                    ),
                }

        return None

    @staticmethod
    def _normalize_external_integration(
        value,
    ) -> dict[str, Any]:

        if not isinstance(
            value,
            dict,
        ):
            value = {}

        providers = (
            value.get(
                "providers",
                [],
            )
            or []
        )

        if isinstance(
            providers,
            str,
        ):
            providers = [
                providers
            ]

        return {
            "requested":
                bool(
                    value.get(
                        "requested",
                        False,
                    )
                ),

            "connected":
                bool(
                    value.get(
                        "connected",
                        False,
                    )
                ),

            "status":
                value.get(
                    "status",
                    "NOT_REQUESTED",
                ),

            "providers":
                list(
                    dict.fromkeys(
                        str(provider)
                        for provider in providers
                        if provider
                    )
                ),

            "evidence_count":
                max(
                    0,
                    int(
                        value.get(
                            "evidence_count",
                            0,
                        )
                        or 0
                    ),
                ),
        }

    @staticmethod
    def _default_external_integration():
        return {
            "requested": False,
            "connected": False,
            "status": "NOT_REQUESTED",
            "providers": [],
            "evidence_count": 0,
        }

    # --------------------------------------------------
    # Proof Evidence Projection
    # --------------------------------------------------

    @staticmethod
    def _proof_evidence_item(
        item,
    ):
        if not isinstance(
            item,
            dict,
        ):
            return None

        return {
            "type":
                item.get(
                    "type",
                    "UNKNOWN",
                ),

            "path":
                item.get(
                    "path",
                ),

            "relevance":
                item.get(
                    "relevance",
                    "UNKNOWN",
                ),

            "strength":
                item.get(
                    "evidence_strength",
                    item.get(
                        "strength",
                        "UNKNOWN",
                    ),
                ),

            "score":
                item.get(
                    "relevance_score",
                    item.get(
                        "score",
                        0,
                    ),
                ),

            "role":
                item.get(
                    "selection_role",
                    item.get(
                        "role",
                        "UNKNOWN",
                    ),
                ),

            "excerpt":
                item.get(
                    "excerpt",
                    "",
                ),
        }

    # ==================================================
    # Proof Status
    # ==================================================

    @staticmethod
    def _proof_status(
        execution,
        verification,
        outcome,
    ) -> str:

        if outcome.get(
            "status"
        ) == "SUCCESSFUL":

            return "PROVEN"

        if verification.get(
            "status"
        ) == "VERIFIED":

            return "VERIFIED"

        if execution.get(
            "performed"
        ):

            return "PARTIAL"

        return "INCOMPLETE"