"""
Graphify

Phase 38
Stage 38.8

Evidence Relevance Engine

Ranks already-observed repository evidence against existing
canonical engineering meaning.

This is a read-only projection/classification layer.

It MUST NOT:

- create decisions
- modify decisions
- create policy
- create plans
- create memory
- execute repository work
- mutate repository files
- infer causality

Relevance and evidentiary strength are intentionally separate.

    relevance
        How related is this artifact to the current decision?

    strength
        How directly does the artifact support the decision?

Author:
Graphify Core
"""

from __future__ import annotations

from typing import Any


class EvidenceRelevanceEngine:

    VERSION = "38.8.1"

    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"

    EXPLICIT = "EXPLICIT"
    DIRECT = "DIRECT"
    INDIRECT = "INDIRECT"
    HISTORICAL = "HISTORICAL"
    DERIVED = "DERIVED"
    WEAK = "WEAK"

    # ==================================================
    # Public API
    # ==================================================

    def rank(
        self,
        evidence: dict[str, Any],
        decision: Any,
        plan: Any,
    ) -> dict[str, Any]:
        """
        Rank already-collected evidence against canonical
        engineering meaning.

        No repository access occurs here.
        """

        if not isinstance(
            evidence,
            dict,
        ):
            raise TypeError(
                "evidence must be a dictionary."
            )

        decision_data = self._as_dict(
            decision
        )

        plan_data = self._as_dict(
            plan
        )

        decision_terms = self._terms(
            decision_data
        )

        plan_terms = self._terms(
            plan_data
        )

        # --------------------------------------------------
        # Flatten evidence sources
        # --------------------------------------------------

        flattened = []

        for category in (
            "direct",
            "related",
            "context",
            "repository_files",
        ):

            items = (
                evidence.get(
                    category,
                    [],
                )
                or []
            )

            if not isinstance(
                items,
                list,
            ):
                continue

            for item in items:

                if not isinstance(
                    item,
                    dict,
                ):
                    continue

                flattened.append(
                    self._copy_item(
                        item,
                        category,
                    )
                )

        # --------------------------------------------------
        # Deduplicate repository artifacts
        # --------------------------------------------------

        deduplicated = self._deduplicate(
            flattened
        )

        ranked = []

        for item in deduplicated:

            ranked.append(
                self._rank_item(
                    item=item,
                    decision_terms=decision_terms,
                    plan_terms=plan_terms,
                )
            )

        ranked.sort(
            key=self._sort_key,
            reverse=True,
        )

        high = [
            item
            for item in ranked
            if item.get(
                "relevance"
            ) == self.HIGH
        ]

        medium = [
            item
            for item in ranked
            if item.get(
                "relevance"
            ) == self.MEDIUM
        ]

        low = [
            item
            for item in ranked
            if item.get(
                "relevance"
            ) == self.LOW
        ]

        return {

            "status":
                "success",

            "version":
                self.VERSION,

            "evidence_count":
                len(ranked),

            "ranked_evidence":
                ranked,

            "high_relevance":
                high,

            "medium_relevance":
                medium,

            "low_relevance":
                low,

            "summary": {

                "high":
                    len(high),

                "medium":
                    len(medium),

                "low":
                    len(low),

            },

            "provenance": {

                "read_only":
                    True,

                "decision_authority":
                    False,

                "policy_authority":
                    False,

                "planning_authority":
                    False,

                "execution_authority":
                    False,

                "memory_authority":
                    False,

                "causality_inference":
                    False,

                "repository_mutation":
                    False,

            },

        }

    # ==================================================
    # Ranking
    # ==================================================

    def _rank_item(
        self,
        item: dict[str, Any],
        decision_terms: set[str],
        plan_terms: set[str],
    ) -> dict[str, Any]:

        evidence_type = str(
            item.get(
                "type",
                "",
            )
        ).lower()

        path = str(
            item.get(
                "path",
                "",
            )
        )

        normalized_path = (
            path
            .lower()
            .replace(
                "\\",
                "/",
            )
        )

        message = str(
            item.get(
                "message",
                "",
            )
        )

        title = str(
            item.get(
                "title",
                "",
            )
        )

        description = str(
            item.get(
                "description",
                "",
            )
        )

        text = " ".join(
            [
                evidence_type,
                normalized_path,
                message,
                title,
                description,
                str(
                    item.get(
                        "text",
                        "",
                    )
                ),
            ]
        ).lower()

        text_terms = self._normalize_terms(
            text
        )

        decision_overlap = (
            text_terms
            &
            decision_terms
        )

        plan_overlap = (
            text_terms
            &
            plan_terms
        )

        score = 0
        signals = []
        strength = self.WEAK

        # --------------------------------------------------
        # Explicit decision evidence
        # --------------------------------------------------

        explicit_decision = (
            self._contains_explicit_decision(
                text,
                normalized_path,
                evidence_type,
            )
        )

        explicit_canonical_match = (
            self._contains_explicit_canonical_match(
                text,
                decision_terms,
            )
        )

        if explicit_decision:

            score += 6

            strength = self.EXPLICIT

            signals.append(
                "explicit decision artifact"
            )

        if explicit_canonical_match:

            score += 6

            strength = self.EXPLICIT

            signals.append(
                "explicit canonical decision match"
            )

        # --------------------------------------------------
        # Canonical decision overlap
        # --------------------------------------------------

        if decision_overlap:

            score += min(
                5,
                len(
                    decision_overlap
                ) * 2,
            )

            if strength == self.WEAK:

                strength = self.DIRECT

            signals.append(
                "canonical decision-term overlap"
            )

        # --------------------------------------------------
        # Canonical plan overlap
        # --------------------------------------------------

        if plan_overlap:

            score += min(
                4,
                len(
                    plan_overlap
                ),
            )

            if strength == self.WEAK:

                strength = self.INDIRECT

            signals.append(
                "canonical plan-term overlap"
            )

        # --------------------------------------------------
        # ADR structure
        # --------------------------------------------------

        if self._is_adr_path(
            normalized_path
        ):

            score += 4

            if strength == self.WEAK:

                strength = self.DIRECT

            signals.append(
                "ADR document structure"
            )

        # --------------------------------------------------
        # Architecture documentation
        # --------------------------------------------------
        #
        # Important:
        # Merely mentioning "architecture" is NOT enough.
        # The document must also have meaningful canonical
        # overlap or explicit decision structure.
        #
        # This prevents generic READMEs from ranking highly.
        #

        if self._is_architecture_document(
            normalized_path,
            text,
        ):

            strong_decision_overlap = (
                len(
                    decision_overlap
                ) >= 2
            )

            strong_plan_overlap = bool(
                plan_overlap
            )

            if (
                explicit_decision
                or strong_decision_overlap
                or strong_plan_overlap
            ):

                score += 3

                if strength == self.WEAK:

                    strength = self.DIRECT

                signals.append(
                    "architecture documentation"
                )

            else:

                signals.append(
                    "architecture documentation without strong canonical overlap"
                )

        # --------------------------------------------------
        # Architecture source
        # --------------------------------------------------

        if self._is_architecture_source(
            normalized_path
        ):

            score += 1

            if strength == self.WEAK:

                strength = self.INDIRECT

            signals.append(
                "architecture-related source"
            )

        # --------------------------------------------------
        # Historical Git commit
        # --------------------------------------------------

        if evidence_type in {
            "git_commit",
            "commit",
        }:

            score += 1

            if strength == self.WEAK:

                strength = self.HISTORICAL

            signals.append(
                "historical commit evidence"
            )

        # --------------------------------------------------
        # Current Git diff
        # --------------------------------------------------

        if evidence_type in {
            "git_diff",
            "diff",
        }:

            score += 1

            if strength == self.WEAK:

                strength = self.INDIRECT

            signals.append(
                "current repository change evidence"
            )

        # --------------------------------------------------
        # Generated artifacts
        # --------------------------------------------------

        if self._is_generated_artifact(
            normalized_path
        ):

            score -= 4

            strength = self.DERIVED

            signals.append(
                "generated artifact"
            )

        # --------------------------------------------------
        # Test artifacts
        # --------------------------------------------------

        if self._is_test_artifact(
            normalized_path
        ):

            score -= 1

            signals.append(
                "test artifact"
            )

        # --------------------------------------------------
        # Relevance classification
        # --------------------------------------------------

        if score >= 8:

            relevance = self.HIGH

        elif score >= 3:

            relevance = self.MEDIUM

        else:

            relevance = self.LOW

        # Explicit canonical evidence is always HIGH.
        if explicit_canonical_match:

            relevance = self.HIGH

        return {

            **item,

            "relevance":
                relevance,

            "relevance_score":
                score,

            "evidence_strength":
                strength,

            "relevance_signals":
                signals,

            "decision_term_overlap":
                sorted(
                    decision_overlap
                ),

            "plan_term_overlap":
                sorted(
                    plan_overlap
                ),

            "causality_status":
                "NOT_INFERRED",

        }

    # ==================================================
    # Explicit Decision Detection
    # ==================================================

    @staticmethod
    def _contains_explicit_decision(
        text: str,
        path: str,
        evidence_type: str,
    ) -> bool:

        if evidence_type in {
            "adr",
            "architecture_decision",
            "decision_record",
            "repository_decision",
        }:

            return True

        markers = (
            "## architecture decision",
            "architecture decision:",
            "decision:",
            "decision :",
            "selected goal:",
            "selected_goal:",
            "canonical decision:",
        )

        if any(
            marker in text
            for marker in markers
        ):

            return True

        return (
            "/adr/" in path
            or path.startswith("adr-")
            or "/adr-" in path
        )

    @staticmethod
    def _contains_explicit_canonical_match(
        text: str,
        decision_terms: set[str],
    ) -> bool:

        important_terms = {
            term
            for term in decision_terms
            if len(term) >= 5
        }

        if not important_terms:

            return False

        overlap = (
            important_terms
            &
            EvidenceRelevanceEngine._normalize_terms(
                text
            )
        )

        return len(
            overlap
        ) >= 2

    # ==================================================
    # Artifact Classification
    # ==================================================

    @staticmethod
    def _is_adr_path(
        path: str,
    ) -> bool:

        return (
            "/adr/" in path
            or path.startswith("adr-")
            or "/adr-" in path
            or path.endswith(
                "adr.md"
            )
        )

    @staticmethod
    def _is_architecture_document(
        path: str,
        text: str,
    ) -> bool:

        extensions = (
            ".md",
            ".rst",
            ".txt",
            ".adoc",
        )

        if not path.endswith(
            extensions
        ):

            return False

        markers = (
            "architecture",
            "architectural",
            "system design",
            "component design",
        )

        return any(
            marker in path
            or marker in text
            for marker in markers
        )

    @staticmethod
    def _is_architecture_source(
        path: str,
    ) -> bool:

        tokens = (
            "architecture",
            "architect",
            "design",
            "topology",
            "structure",
        )

        return any(
            token in path
            for token in tokens
        )

    @staticmethod
    def _is_generated_artifact(
        path: str,
    ) -> bool:

        tokens = (
            "graphify-out/",
            "graph.json",
            "symbol_index.json",
            "uacs.json",
            "future_roadmap.json",
            "project_prediction.json",
            "repository_dashboard.json",
            "ai_handover",
            "repository_context.graphify",
            "repository_context.gctx",
        )

        return any(
            token in path
            for token in tokens
        )

    @staticmethod
    def _is_test_artifact(
        path: str,
    ) -> bool:

        return (
            path.startswith(
                "tests/"
            )
            or "/tests/" in path
        )

    # ==================================================
    # Deduplication
    # ==================================================

    @staticmethod
    def _copy_item(
        item: dict[str, Any],
        category: str,
    ) -> dict[str, Any]:

        result = dict(
            item
        )

        result[
            "_source_categories"
        ] = [
            category
        ]

        return result

    @staticmethod
    def _deduplicate(
        items: list[dict[str, Any]],
    ) -> list[dict[str, Any]]:

        unique = {}

        for item in items:

            key = (
                EvidenceRelevanceEngine
                ._identity_key(
                    item
                )
            )

            if key not in unique:

                unique[key] = item

                continue

            existing = unique[key]

            categories = list(
                existing.get(
                    "_source_categories",
                    [],
                )
            )

            incoming = item.get(
                "_source_categories",
                [],
            )

            for category in incoming:

                if category not in categories:

                    categories.append(
                        category
                    )

            existing[
                "_source_categories"
            ] = categories

        return list(
            unique.values()
        )

    @staticmethod
    def _identity_key(
        item: dict[str, Any],
    ) -> tuple:

        path = item.get(
            "path",
            "",
        )

        commit = item.get(
            "commit",
            "",
        )

        evidence_type = item.get(
            "type",
            "",
        )

        message = item.get(
            "message",
            "",
        )

        if path:

            return (
                "path",
                str(
                    path
                ).replace(
                    "\\",
                    "/",
                ).lower(),
            )

        if commit:

            return (
                "commit",
                str(commit),
            )

        return (
            evidence_type,
            message,
        )

    # ==================================================
    # Helpers
    # ==================================================

    @staticmethod
    def _as_dict(
        value: Any,
    ) -> dict[str, Any]:

        if isinstance(
            value,
            dict,
        ):

            return value

        to_dict = getattr(
            value,
            "to_dict",
            None,
        )

        if callable(
            to_dict
        ):

            try:

                result = to_dict()

                if isinstance(
                    result,
                    dict,
                ):

                    return result

            except Exception:

                pass

        return {}

    @classmethod
    def _terms(
        cls,
        value: dict[str, Any],
    ) -> set[str]:

        parts = []

        for key in (
            "selected_goal",
            "decision",
            "strategic_focus",
            "policy_action",
            "objective",
            "engineering_strategy",
            "expected_result",
        ):

            current = value.get(
                key
            )

            if current is not None:

                parts.append(
                    str(current)
                )

        return cls._normalize_terms(
            " ".join(
                parts
            )
        )

    @staticmethod
    def _normalize_terms(
        text: str,
    ) -> set[str]:

        words = []
        current = []

        for character in text.lower():

            if character.isalnum():

                current.append(
                    character
                )

            else:

                if current:

                    words.append(
                        "".join(
                            current
                        )
                    )

                    current = []

        if current:

            words.append(
                "".join(
                    current
                )
            )

        stop_words = {
            "the",
            "and",
            "or",
            "to",
            "of",
            "a",
            "an",
            "is",
            "for",
            "with",
            "from",
            "on",
            "in",
            "repository",
            "engineering",
            "current",
            "result",
            "continuous",
            "improvement",
        }

        return {
            word
            for word in words
            if len(word) >= 3
            and word not in stop_words
        }

    @staticmethod
    def _sort_key(
        item: dict[str, Any],
    ) -> tuple:

        relevance_order = {
            "HIGH": 3,
            "MEDIUM": 2,
            "LOW": 1,
        }

        strength_order = {
            "EXPLICIT": 6,
            "DIRECT": 5,
            "INDIRECT": 4,
            "HISTORICAL": 3,
            "DERIVED": 2,
            "WEAK": 1,
        }

        return (
            relevance_order.get(
                item.get(
                    "relevance",
                    "LOW",
                ),
                0,
            ),
            strength_order.get(
                item.get(
                    "evidence_strength",
                    "WEAK",
                ),
                0,
            ),
            item.get(
                "relevance_score",
                0,
            ),
            str(
                item.get(
                    "path",
                    "",
                )
            ),
        )