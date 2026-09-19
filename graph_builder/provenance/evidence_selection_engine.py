"""
Graphify

Phase 38
Stage 38.11

Evidence Selection Engine

Selects a small, decision-useful and diverse subset from
already-ranked repository evidence.

This layer does not create evidence, decisions, plans, policy,
memory, or causality.

Relevance scores and evidence strength are preserved.
"""

from __future__ import annotations

from typing import Any


class EvidenceSelectionEngine:

    VERSION = "38.11.3"

    DEFAULT_LIMIT = 5

    ROLE_PRIORITY = (
        "DECISION",
        "ARCHITECTURE",
        "RISK",
        "CHANGE",
        "HISTORICAL",
        "VERIFICATION",
        "IMPLEMENTATION",
        "DOCUMENTATION",
        "OTHER",
    )

    ROLE_LIMITS = {
        "DECISION": 1,
        "IMPLEMENTATION": 1,
        "ARCHITECTURE": 1,
        "RISK": 1,
        "CHANGE": 1,
        "HISTORICAL": 1,
        "VERIFICATION": 1,
        "DOCUMENTATION": 1,
        "OTHER": 1,
    }

    def select(
        self,
        ranked_result: dict[str, Any],
        limit: int = DEFAULT_LIMIT,
    ) -> dict[str, Any]:

        if not isinstance(
            ranked_result,
            dict,
        ):
            raise TypeError(
                "ranked_result must be a dictionary."
            )

        try:
            limit = int(
                limit
            )
        except (
            TypeError,
            ValueError,
        ):
            limit = self.DEFAULT_LIMIT

        if limit < 1:
            limit = self.DEFAULT_LIMIT

        ranked = (
            ranked_result.get(
                "ranked_evidence",
                [],
            )
            or []
        )

        candidates = [
            item
            for item in ranked
            if isinstance(
                item,
                dict,
            )
        ]

        selected = []
        used_paths = set()
        used_roles = set()

        # --------------------------------------------------
        # Pass 1
        # Prefer one meaningful artifact from different roles.
        #
        # Weak or zero-score evidence is never customer-facing.
        # --------------------------------------------------

        for preferred_role in self.ROLE_PRIORITY:

            if len(selected) >= limit:
                break

            for item in candidates:

                relevance = str(
                    item.get(
                        "relevance",
                        "LOW",
                    )
                ).upper()

                score = item.get(
                    "relevance_score",
                    0,
                )

                try:
                    score = float(
                        score
                    )
                except (
                    TypeError,
                    ValueError,
                ):
                    score = 0

                if (
                    relevance == "LOW"
                    or score <= 0
                ):
                    continue

                role = self._role(
                    item
                )

                if role != preferred_role:
                    continue

                path = self._path(
                    item
                )

                if path in used_paths:
                    continue

                if role in used_roles:
                    continue

                selected.append(
                    self._annotate(
                        item,
                        role=role,
                        reason=self._selection_reason(
                            role
                        ),
                    )
                )

                used_paths.add(
                    path
                )

                used_roles.add(
                    role
                )

                break

        # --------------------------------------------------
        # Pass 2
        # Fill remaining slots by relevance rank while
        # avoiding duplicate artifacts and over-saturation.
        #
        # Weak or zero-score evidence is rejected here too.
        # --------------------------------------------------

        for item in candidates:

            if len(selected) >= limit:
                break

            relevance = str(
                item.get(
                    "relevance",
                    "LOW",
                )
            ).upper()

            score = item.get(
                "relevance_score",
                0,
            )

            try:
                score = float(
                    score
                )
            except (
                TypeError,
                ValueError,
            ):
                score = 0

            if (
                relevance == "LOW"
                or score <= 0
            ):
                continue

            path = self._path(
                item
            )

            if path in used_paths:
                continue

            role = self._role(
                item
            )

            role_limit = self.ROLE_LIMITS.get(
                role,
                1,
            )

            role_count = sum(
                1
                for selected_item in selected
                if selected_item.get(
                    "selection_role"
                ) == role
            )

            if role_count >= role_limit:
                continue

            selected.append(
                self._annotate(
                    item,
                    role=role,
                    reason=self._selection_reason(
                        role
                    ),
                )
            )

            used_paths.add(
                path
            )

        return {

            "version":
                self.VERSION,

            "status":
                "SELECTED",

            "selected_evidence":
                selected,

            "selected_count":
                len(selected),

            "available_count":
                len(candidates),

            "selection_limit":
                limit,

            "selection_policy": {

                "diversity_first":
                    True,

                "maximum_items_per_role":
                    1,

                "weak_evidence_rejected":
                    True,

                "zero_score_evidence_rejected":
                    True,

                "relevance_preserved":
                    True,

                "scores_modified":
                    False,

                "causality_inferred":
                    False,

                "read_only":
                    True,

            },

            "provenance": {

                "source":
                    "EvidenceRelevanceEngine",

                "selection_layer":
                    "EvidenceSelectionEngine",

                "creates_decision":
                    False,

                "creates_plan":
                    False,

                "creates_memory":
                    False,

                "executes_work":
                    False,

                "mutates_repository":
                    False,

                "causality_inference":
                    False,

            },

        }

    @staticmethod
    def _path(
        item,
    ) -> str:

        path = item.get(
            "path"
        )

        if path:
            return (
                str(
                    path
                )
                .replace(
                    "\\",
                    "/",
                )
                .lower()
            )

        commit = item.get(
            "commit"
        )

        if commit:
            return (
                f"commit:{commit}"
            )

        return repr(
            item
        )

    @classmethod
    def _role(
        cls,
        item,
    ) -> str:

        evidence_type = str(
            item.get(
                "type",
                "",
            )
        ).lower()

        path = (
            str(
                item.get(
                    "path",
                    "",
                )
            )
            .replace(
                "\\",
                "/",
            )
            .lower()
        )

        signals = " ".join(
            str(signal).lower()
            for signal in (
                item.get(
                    "relevance_signals",
                    [],
                )
                or []
            )
        )

        strength = str(
            item.get(
                "evidence_strength",
                "",
            )
        ).upper()

        # --------------------------------------------------
        # Decision evidence
        # --------------------------------------------------
        #
        # Only actual decision artifacts should consume the
        # DECISION role. Evidence strength must not determine
        # semantic role.
        #

        if (
            evidence_type
            == "repository_document"
            and (
                "adr-" in path
                or path.startswith("adr")
                or "/adr/" in path
                or "decision" in path
            )
        ):
            return "DECISION"

        # --------------------------------------------------
        # Historical evidence
        # --------------------------------------------------

        if (
            evidence_type
            == "git_commit"
        ):
            return "HISTORICAL"

        # --------------------------------------------------
        # Change evidence
        # --------------------------------------------------

        if (
            evidence_type
            == "git_diff"
        ):
            return "CHANGE"

        # --------------------------------------------------
        # Verification evidence
        # --------------------------------------------------

        if (
            path.startswith(
                "tests/"
            )
            or "/tests/" in path
            or "test artifact" in signals
        ):
            return "VERIFICATION"

        # --------------------------------------------------
        # Risk evidence
        # --------------------------------------------------

        if any(
            token in path
            for token in (
                "risk",
                "diagnostic",
                "hotspot",
                "criticality",
            )
        ):
            return "RISK"

        # --------------------------------------------------
        # Architecture evidence
        # --------------------------------------------------

        if any(
            token in path
            for token in (
                "architecture",
            )
        ):
            return "ARCHITECTURE"

        # --------------------------------------------------
        # Implementation evidence
        # --------------------------------------------------

        if (
            evidence_type
            == "repository_file"
        ):
            return "IMPLEMENTATION"

        # --------------------------------------------------
        # Explicit documentation
        # --------------------------------------------------

        if (
            evidence_type
            == "repository_document"
        ):
            return "DOCUMENTATION"

        return "OTHER"

    @staticmethod
    def _selection_reason(
        role: str,
    ) -> str:

        reasons = {
            "DECISION":
                "selected because it directly supports the current decision",

            "ARCHITECTURE":
                "selected because it provides relevant architecture evidence",

            "RISK":
                "selected because it provides relevant risk evidence",

            "CHANGE":
                "selected because it provides relevant change evidence",

            "HISTORICAL":
                "selected as historical evidence supporting the current decision",

            "VERIFICATION":
                "selected because it provides relevant verification evidence",

            "IMPLEMENTATION":
                "selected because it provides relevant implementation evidence",

            "DOCUMENTATION":
                "selected because it provides relevant documentation evidence",

            "OTHER":
                "selected because it provides relevant supporting evidence",
        }

        return reasons.get(
            role,
            "selected because it provides relevant supporting evidence",
        )

    @staticmethod
    def _annotate(
        item,
        role,
        reason,
    ):

        result = dict(
            item
        )

        result[
            "selection_role"
        ] = role

        result[
            "selection_reason"
        ] = reason

        result[
            "selection_layer"
        ] = (
            "EvidenceSelectionEngine"
        )

        return result