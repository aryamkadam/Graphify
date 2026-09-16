"""
Graphify

Phase 38
Stage 38.11

Customer-Facing Engineering Review

Presentation-only projection over the canonical provenance chain.

Flow:

    EngineeringDecisionRecord
            ↓
    EvidenceRelevanceEngine
            ↓
    EvidenceSelectionEngine
            ↓
    EngineeringReview

This component does not create decisions, plans, policy, memory,
or engineering work.

It does not infer causality.
It does not modify repository state.
It does not alter evidence relevance scores.
It does not determine external integration state.

External integration metadata is read from the canonical
EngineeringDecisionRecord and projected without inference.
"""

from __future__ import annotations

from graph_builder.provenance.evidence_selection_engine import (
    EvidenceSelectionEngine,
)

from graph_builder.provenance.evidence_relevance_engine import (
    EvidenceRelevanceEngine,
)


class EngineeringReview:

    VERSION = "38.11"

    DEFAULT_LIMIT = 5

    DEFAULT_EXTERNAL_INTEGRATION = {
        "requested": False,
        "connected": False,
        "status": "NOT_REQUESTED",
        "providers": [],
        "evidence_count": 0,
    }

    # ==================================================
    # Public API
    # ==================================================

    def build(
        self,
        record,
        limit=DEFAULT_LIMIT,
        execution=None,
    ):
        """
        Build a concise customer-facing engineering review.

        The supplied EngineeringDecisionRecord remains the source
        of canonical decision meaning, observed evidence, and
        external integration metadata.

        Evidence is ranked by the existing EvidenceRelevanceEngine.
        EvidenceSelectionEngine controls presentation selection.

        External integration state is projected only. This layer
        does not connect to providers, fetch evidence, or infer
        connectivity from evidence presence.
        """

        if not isinstance(
            record,
            dict,
        ):
            raise TypeError(
                "record must be a dictionary."
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

        raw_evidence = (
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

        execution_data = (
            execution
            if isinstance(
                execution,
                dict,
            )
            else None
        )

        execution_performed = bool(
            execution_data
            and execution_data.get(
                "execution_performed",
                False,
            )
        )

        execution_result = (
            execution_data.get(
                "execution",
                {},
            )
            if execution_performed
            else {}
        )

        if not isinstance(
            execution_result,
            dict,
        ):

            execution_result = {}

        accountability = (
            execution_data.get(
                "accountability"
            )
            if execution_performed
            else None
        )

        outcome_memory = (
            execution_data.get(
                "outcome_memory"
            )
            if execution_performed
            else None
        )

        # --------------------------------------------------
        # Existing relevance layer
        # --------------------------------------------------

        ranked = (
            self._rank_evidence(
                raw_evidence=
                    raw_evidence,
                decision=
                    decision,
                plan=
                    plan,
            )
        )

        ranked_items = (
            ranked.get(
                "ranked_evidence",
                [],
            )
            or []
        )

        # --------------------------------------------------
        # Select presentation evidence
        # --------------------------------------------------

        selection = (
            EvidenceSelectionEngine().select(
                ranked_result=ranked,
                limit=limit,
            )
        )

        selected = (
            selection.get(
                "selected_evidence",
                [],
            )
            or []
        )

        # --------------------------------------------------
        # Evidence totals
        # --------------------------------------------------

        evidence_available = (
            self._evidence_count(
                raw_evidence,
                ranked,
            )
        )

        summary = (
            ranked.get(
                "summary",
                {},
            )
            or {}
        )

        # --------------------------------------------------
        # Execution projection
        # --------------------------------------------------

        execution_projection = (
            self._execution_projection(
                execution=
                    execution_data,
                execution_result=
                    execution_result,
                accountability=
                    accountability,
                outcome_memory=
                    outcome_memory,
            )
        )

        # --------------------------------------------------
        # External integration projection
        # --------------------------------------------------

        external_integration = (
            self._external_integration_projection(
                record=record,
                provenance=provenance,
                knowledge=knowledge,
                raw_evidence=raw_evidence,
            )
        )

        # --------------------------------------------------
        # Trust boundary
        # --------------------------------------------------

        return {

            "version":
                self.VERSION,

            "status":
                "READY",

            "repository":
                record.get(
                    "repository"
                ),

            "decision":
                decision.get(
                    "decision",
                    "UNKNOWN",
                ),

            "selected_goal":
                decision.get(
                    "selected_goal",
                    "UNKNOWN",
                ),

            "strategic_focus":
                decision.get(
                    "strategic_focus",
                    "UNKNOWN",
                ),

            "plan_objective":
                plan.get(
                    "objective",
                    "UNKNOWN",
                ),

            "engineering_strategy":
                plan.get(
                    "engineering_strategy",
                    "UNKNOWN",
                ),

            "expected_result":
                plan.get(
                    "expected_result",
                    "UNKNOWN",
                ),

            "evidence":
                self._presentation_evidence(
                    selected
                ),

            "evidence_shown":
                len(
                    selected
                ),

            "evidence_available":
                evidence_available,

            "relevance_summary": {

                "high":
                    summary.get(
                        "high",
                        0,
                    ),

                "medium":
                    summary.get(
                        "medium",
                        0,
                    ),

                "low":
                    summary.get(
                        "low",
                        0,
                    ),

            },

            "external_integration":
                external_integration,

            "execution":
                execution_projection,

            "outcome":
                (
                    execution_projection.get(
                        "outcome",
                        "UNKNOWN",
                    )
                    if execution_projection.get(
                        "performed",
                        False,
                    )
                    else knowledge.get(
                        "outcome",
                        "UNKNOWN",
                    )
                ),

            "outcome_reason":
                self._outcome_reason(
                    knowledge,
                    execution_projection,
                ),

            "trust": {

                "causality_inferred":
                    False,

                "repository_mutated":
                    provenance.get(
                        "mutates_repository",
                        False,
                    ),

                "selection_version":
                    selection.get(
                        "version",
                        "UNKNOWN",
                    ),

                "selection_policy":
                    selection.get(
                        "selection_policy",
                        {},
                    ),

                "decision_created":
                    provenance.get(
                        "creates_decision",
                        False,
                    ),

                "plan_created":
                    provenance.get(
                        "creates_plan",
                        False,
                    ),

                "work_executed":
                    execution_projection.get(
                        "performed",
                        False,
                    ),

            },

            "provenance": {

                "source":
                    "EngineeringDecisionRecord",

                "relevance_owner":
                    "EvidenceRelevanceEngine",

                "review_layer":
                    "EngineeringReview",

                "read_only":
                    True,

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

    # ==================================================
    # External Integration Projection
    # ==================================================

    @classmethod
    def _external_integration_projection(
        cls,
        record,
        provenance,
        knowledge,
        raw_evidence,
    ):
        """
        Project canonical external integration metadata.

        This method MUST NOT infer integration state from the mere
        presence or absence of external evidence.

        Preferred source:

            EngineeringDecisionRecord.external_integration

        Compatibility fallbacks exist for older records that may
        only contain the previous provenance fields.
        """

        integration = None

        # --------------------------------------------------
        # Preferred canonical location
        # --------------------------------------------------

        for container in (
            record,
            provenance,
            knowledge,
        ):

            if not isinstance(
                container,
                dict,
            ):
                continue

            candidate = container.get(
                "external_integration"
            )

            if isinstance(
                candidate,
                dict,
            ):

                integration = candidate
                break

        # --------------------------------------------------
        # Preferred canonical object available
        # --------------------------------------------------

        if integration is not None:

            requested = bool(
                integration.get(
                    "requested",
                    False,
                )
            )

            connected = bool(
                integration.get(
                    "connected",
                    False,
                )
            )

            status = integration.get(
                "status",
                "NOT_REQUESTED",
            )

            providers = (
                integration.get(
                    "providers",
                    [],
                )
                or []
            )

            evidence_count = (
                integration.get(
                    "evidence_count",
                    0,
                )
            )

            return cls._normalize_external_integration(
                requested=requested,
                connected=connected,
                status=status,
                providers=providers,
                evidence_count=evidence_count,
            )

        # --------------------------------------------------
        # Compatibility fallback
        #
        # This supports older EngineeringDecisionRecord
        # instances that predate external_integration.
        # --------------------------------------------------

        providers = (
            provenance.get(
                "external_providers",
                [],
            )
            or []
        )

        if not providers:

            providers = (
                provenance.get(
                    "external_provider",
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

        providers = [
            str(provider)
            for provider
            in providers
            if provider
        ]

        statuses = (
            provenance.get(
                "external_statuses",
                [],
            )
            or []
        )

        if isinstance(
            statuses,
            str,
        ):

            statuses = [
                statuses
            ]

        status = (
            statuses[0]
            if statuses
            else "NOT_REQUESTED"
        )

        legacy_requested = bool(
            provenance.get(
                "external_evidence",
                False,
            )
        ) or bool(
            providers
        )

        legacy_external = (
            raw_evidence.get(
                "external",
                [],
            )
            or []
            if isinstance(
                raw_evidence,
                dict,
            )
            else []
        )

        legacy_evidence_count = len(
            legacy_external
            if isinstance(
                legacy_external,
                list,
            )
            else []
        )

        # --------------------------------------------------
        # Only explicit canonical status determines
        # connectivity in the compatibility path.
        # --------------------------------------------------

        connected_statuses = {
            "CONNECTED_WITH_EVIDENCE",
            "CONNECTED_NO_EVIDENCE",
        }

        connected = (
            status in connected_statuses
        )

        return cls._normalize_external_integration(
            requested=legacy_requested,
            connected=connected,
            status=status,
            providers=providers,
            evidence_count=legacy_evidence_count,
        )

    @staticmethod
    def _normalize_external_integration(
        requested,
        connected,
        status,
        providers,
        evidence_count,
    ):
        """
        Normalize external integration metadata without changing
        its semantic meaning.
        """

        if not isinstance(
            providers,
            list,
        ):

            if providers is None:
                providers = []

            else:
                providers = [
                    providers
                ]

        normalized_providers = []

        for provider in providers:

            if provider is None:
                continue

            provider = str(
                provider
            ).strip()

            if not provider:
                continue

            if provider not in normalized_providers:

                normalized_providers.append(
                    provider
                )

        try:

            normalized_evidence_count = int(
                evidence_count
            )

        except (
            TypeError,
            ValueError,
        ):

            normalized_evidence_count = 0

        normalized_evidence_count = max(
            0,
            normalized_evidence_count,
        )

        normalized_status = (
            str(status).strip()
            if status is not None
            else "UNKNOWN"
        )

        if not normalized_status:
            normalized_status = "UNKNOWN"

        return {

            "requested":
                bool(
                    requested
                ),

            "connected":
                bool(
                    connected
                ),

            "status":
                normalized_status,

            "providers":
                normalized_providers,

            "evidence_count":
                normalized_evidence_count,

        }

    # ==================================================
    # Execution Projection
    # ==================================================

    @staticmethod
    def _execution_projection(
        execution,
        execution_result,
        accountability,
        outcome_memory,
    ):
        """
        Project existing canonical execution information.

        Canonical flat execution fields are preferred.
        Compatibility fallbacks support older nested execution
        structures.

        This method does not create, infer, or modify execution
        semantics.
        """

        if not isinstance(
            execution,
            dict,
        ):
            return {

                "performed":
                    False,

                "status":
                    "NOT_EXECUTED",

                "validation":
                    "NOT_AVAILABLE",

                "review":
                    "NOT_AVAILABLE",

                "accountability":
                    "NOT_AVAILABLE",

                "alignment":
                    "UNKNOWN",

                "outcome":
                    "UNKNOWN",

            }

        if not isinstance(
            execution_result,
            dict,
        ):
            execution_result = {}

        # --------------------------------------------------
        # Performed
        # --------------------------------------------------

        performed = execution.get(
            "execution_performed"
        )

        if performed is None:
            performed = True

        # --------------------------------------------------
        # Execution Status
        #
        # Preferred canonical field:
        #     execution_status
        #
        # Compatibility fallbacks:
        #     execution_result["status"]
        #     execution["status"]
        # --------------------------------------------------

        status = execution.get(
            "execution_status"
        )

        if status is None:
            status = execution_result.get(
                "status"
            )

        if status is None:
            status = execution.get(
                "status",
                "UNKNOWN",
            )

        # --------------------------------------------------
        # Validation
        #
        # Preferred canonical field:
        #     validation_status
        #
        # Compatibility fallback:
        #     execution_result["validation"]["result"]
        # --------------------------------------------------

        validation_status = execution.get(
            "validation_status"
        )

        if validation_status is None:

            validation = execution_result.get(
                "validation"
            )

            if isinstance(
                validation,
                dict,
            ):

                validation_status = validation.get(
                    "result"
                )

        # --------------------------------------------------
        # Review
        #
        # Preferred canonical field:
        #     review_status
        #
        # Compatibility fallback:
        #     execution_result["review"]["final_status"]
        # --------------------------------------------------

        review_status = execution.get(
            "review_status"
        )

        if review_status is None:

            review_data = execution_result.get(
                "review"
            )

            if isinstance(
                review_data,
                dict,
            ):

                review_status = review_data.get(
                    "final_status"
                )

        # --------------------------------------------------
        # Accountability
        #
        # Preferred canonical fields:
        #     accountability_status
        #     accountability_alignment
        #
        # Compatibility fallback:
        #     supplied accountability object
        # --------------------------------------------------

        accountability_status = execution.get(
            "accountability_status"
        )

        if accountability_status is None:

            accountability_status = (
                EngineeringReview
                ._accountability_value(
                    accountability,
                    "status",
                )
            )

        alignment = execution.get(
            "accountability_alignment"
        )

        if alignment is None:

            alignment = (
                EngineeringReview
                ._accountability_value(
                    accountability,
                    "alignment",
                )
            )

        # --------------------------------------------------
        # Outcome
        #
        # Preferred canonical field:
        #     execution_outcome
        #
        # Compatibility fallback:
        #     outcome memory
        # --------------------------------------------------

        outcome = execution.get(
            "execution_outcome"
        )

        if outcome is None:

            outcome = (
                EngineeringReview
                ._extract_outcome(
                    outcome_memory
                )
            )

        # --------------------------------------------------
        # Final projection
        # --------------------------------------------------

        return {

            "performed":
                bool(
                    performed
                ),

            "status":
                status
                or "UNKNOWN",

            "validation":
                validation_status
                or "UNKNOWN",

            "review":
                review_status
                or "UNKNOWN",

            "accountability":
                accountability_status
                or "UNKNOWN",

            "alignment":
                alignment
                or "UNKNOWN",

            "outcome":
                outcome
                or "UNKNOWN",

        }

    @staticmethod
    def _accountability_value(
        accountability,
        key,
    ):

        if accountability is None:
            return None

        if isinstance(
            accountability,
            dict,
        ):

            return accountability.get(
                key
            )

        return getattr(
            accountability,
            key,
            None,
        )

    @staticmethod
    def _extract_outcome(
        outcome_memory,
    ):
        """
        Read an already-recorded outcome.

        Unknown remains UNKNOWN when no explicit outcome
        is available.
        """

        if outcome_memory is None:

            return "UNKNOWN"

        if isinstance(
            outcome_memory,
            dict,
        ):

            outcome = outcome_memory.get(
                "outcome"
            )

            if isinstance(
                outcome,
                dict,
            ):

                value = (
                    outcome.get(
                        "result"
                    )
                    or outcome.get(
                        "status"
                    )
                )

                if value:

                    return value

            if outcome not in (
                None,
                "",
            ):

                return str(
                    outcome
                )

            value = (
                outcome_memory.get(
                    "result"
                )
                or outcome_memory.get(
                    "status"
                )
            )

            if value:

                return str(
                    value
                )

        return "UNKNOWN"

    # ==================================================
    # Evidence Ranking
    # ==================================================

    @staticmethod
    def _rank_evidence(
        raw_evidence,
        decision,
        plan,
    ):
        """
        Reuse the canonical relevance engine.

        No new relevance logic is introduced here.
        """

        if not isinstance(
            raw_evidence,
            dict,
        ):

            return {

                "ranked_evidence":
                    [],

                "summary": {

                    "high":
                        0,

                    "medium":
                        0,

                    "low":
                        0,

                },

            }

        return (
            EvidenceRelevanceEngine().rank(
                evidence=
                    raw_evidence,

                decision=
                    decision,

                plan=
                    plan,
            )
        )

    # ==================================================
    # Presentation Evidence
    # ==================================================

    @staticmethod
    def _presentation_evidence(
        items,
    ):
        """
        Convert selected evidence into a concise
        presentation-only representation.

        The original evidence objects are not modified.

        The full 'text' field is removed from the
        presentation output and replaced with a
        normalized excerpt of up to 240 characters.
        """

        result = []

        for item in items:

            if not isinstance(
                item,
                dict,
            ):
                continue

            entry = dict(
                item
            )

            text = entry.pop(
                "text",
                None,
            )

            if text:

                normalized = (
                    " ".join(
                        str(
                            text
                        ).split()
                    )
                )

                entry[
                    "excerpt"
                ] = (
                    normalized[:240]
                    + (
                        "..."
                        if len(
                            normalized
                        ) > 240
                        else ""
                    )
                )

            result.append(
                entry
            )

        return result

    # ==================================================
    # Evidence Count
    # ==================================================

    @staticmethod
    def _evidence_count(
        raw_evidence,
        ranked,
    ):

        counts = (
            raw_evidence.get(
                "counts",
                {},
            )
            or {}
        )

        total = 0

        for key in (
            "direct",
            "related",
            "context",
        ):

            try:

                total += int(
                    counts.get(
                        key,
                        0,
                    )
                )

            except (
                TypeError,
                ValueError,
            ):

                pass

        if total:

            return total

        ranked_items = (
            ranked.get(
                "ranked_evidence",
                [],
            )
            or []
        )

        return len(
            ranked_items
        )

    # ==================================================
    # Outcome
    # ==================================================

    @staticmethod
    def _outcome_reason(
        knowledge,
        execution_projection=None,
    ):

        if isinstance(
            execution_projection,
            dict,
        ):

            if execution_projection.get(
                "performed"
            ):

                outcome = (
                    execution_projection.get(
                        "outcome",
                        "UNKNOWN",
                    )
                )

                if outcome != "UNKNOWN":

                    return (
                        "Outcome is available from "
                        "the canonical engineering execution."
                    )

                return (
                    "Engineering execution completed or "
                    "was attempted, but no explicit verified "
                    "outcome is available."
                )

        outcome = (
            knowledge.get(
                "outcome",
                "UNKNOWN",
            )
        )

        if outcome != "UNKNOWN":

            return (
                "Verified engineering outcome is available."
            )

        return (
            "No verified engineering outcome is available."
        )