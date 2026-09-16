"""
Graphify

Phase 38
Stage 38.6

Engineering Decision Record

Builds a developer-facing engineering decision record from:

    - canonical RepositoryDecisionReport
    - canonical RepositoryPlan
    - DecisionEvidenceCollector output

This component is a READ-ONLY projection.
It does NOT:

    - create decisions
    - create policy
    - create strategy
    - create plans
    - create memory
    - execute engineering work
    - mutate the repository
    - invent rationale
    - invent alternatives
    - invent outcomes
    - convert correlation into causality

The canonical decision remains owned by:
    RepositoryDecisionEngine

The canonical policy remains owned by:
    RepositoryDecisionPolicy

The canonical plan remains owned by:
    RepositoryExecutionPlanningEngine

Experience remains owned by:
    EngineeringMemory

Author:
Graphify Core
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from graph_builder.provenance.decision_evidence_collector import (
    DecisionEvidenceCollector,
)


class EngineeringDecisionRecord:

    VERSION = "38.6"

    STATUS = "READ_ONLY_RECORD"

    # --------------------------------------------------
    # Initialization
    # --------------------------------------------------

    def __init__(
        self,
        evidence_collector=None,
    ):

        self._evidence_collector = (
            evidence_collector
            if evidence_collector is not None
            else DecisionEvidenceCollector()
        )

    # --------------------------------------------------
    # Public API
    # --------------------------------------------------

    def build(
        self,
        repository_path,
        decision,
        repository_plan=None,
        external_evidence=None,
    ):
        """
        Build a structured engineering decision record.

        All decision meaning is taken from the supplied canonical
        decision object.

        All planning meaning is taken from the supplied canonical
        RepositoryPlan.

        Evidence is collected independently and remains explicitly
        classified.

        External integration state is represented separately from
        external evidence items so that:

            connected + no evidence

        is never confused with:

            not requested

        or:

            integration failure.
        """

        repository = Path(
            repository_path
        ).resolve()

        if not repository.exists():
            raise FileNotFoundError(
                f"Repository path does not exist: {repository}"
            )

        if not repository.is_dir():
            raise NotADirectoryError(
                f"Repository path is not a directory: {repository}"
            )

        if decision is None:
            raise ValueError(
                "decision is required."
            )

        # --------------------------------------------------
        # Evidence Collection
        # --------------------------------------------------

        evidence = (
            self._evidence_collector.collect(

                repository_path=
                    repository,

                decision=
                    decision,

                repository_plan=
                    repository_plan,

                external_evidence=
                    external_evidence,

            )
        )
        actual_evidence = (
            evidence.get(
                "evidence",
                {},
            )
            if isinstance(evidence, dict)
            else {}
        )

        # --------------------------------------------------
        # External Integration Projection
        # --------------------------------------------------

        external_integration = (
            self._external_integration_projection(
                evidence=evidence,
                external_evidence=external_evidence,
            )
        )

        # --------------------------------------------------
        # Canonical Projections
        # --------------------------------------------------

        decision_projection = (
            self._decision_projection(
                decision
            )
        )

        plan_projection = (
            self._plan_projection(
                repository_plan
            )
        )

        knowledge = (
            self._knowledge_projection(
                decision=
                    decision,

                repository_plan=
                    repository_plan,

                evidence=
                    evidence,

                external_integration=
                    external_integration,
            )
        )

        # --------------------------------------------------
        # Record
        # --------------------------------------------------

        return {

            "record_version":
                self.VERSION,

            "status":
                self.STATUS,

            "record_type":
                "Engineering Decision Record",

            "repository":
                repository.name,

            "repository_path":
                str(repository),

            "decision":
                decision_projection,

            "plan":
                plan_projection,

            # --------------------------------------------------
            # Actual evidence remains separate from integration
            # status.
            # --------------------------------------------------

            "evidence":
                actual_evidence,

            "knowledge":
                knowledge,

            "unknowns":
                self._unknowns(
                    decision,
                    repository_plan,
                    evidence,
                ),

            "provenance": {

                "source":
                    (
                        "Canonical Graphify decision, canonical "
                        "RepositoryPlan, and read-only repository evidence"
                    ),

                "decision_authority":
                    "RepositoryDecisionEngine",

                "policy_authority":
                    "RepositoryDecisionPolicy",

                "planning_authority":
                    "RepositoryExecutionPlanningEngine",

                "memory_authority":
                    "EngineeringMemory",

                "execution_authority":
                    "EngineeringKernel",

                "evidence_owner":
                    "DecisionEvidenceCollector",

                # --------------------------------------------------
                # Canonical external integration state.
                #
                # IMPORTANT:
                # This describes the integration itself.
                # It is NOT equivalent to evidence being present.
                # --------------------------------------------------

                "external_integration":
                    external_integration,

                # --------------------------------------------------
                # Backward-compatible provider metadata.
                # --------------------------------------------------

                "external_providers":
                    self._external_providers(
                        evidence,
                        external_evidence,
                    ),

                "external_evidence":
                    bool(
                        self._external_evidence_items(
                            evidence
                        )
                    ),

                # --------------------------------------------------
                # Read-only authority boundaries.
                # --------------------------------------------------

                "read_only":
                    True,

                "creates_decision":
                    False,

                "creates_policy":
                    False,

                "creates_strategy":
                    False,

                "creates_plan":
                    False,

                "creates_memory":
                    False,

                "executes_work":
                    False,

                "mutates_repository":
                    False,
            },

            "trust_policy": {

                "unsupported_rationale":
                    "UNKNOWN",

                "unsupported_alternatives":
                    "UNKNOWN",

                "unsupported_outcomes":
                    "UNKNOWN",

                "unsupported_causality":
                    "UNKNOWN",

                "correlation_is_causality":
                    False,

                "inference_without_evidence":
                    False,

            },

        }

    # --------------------------------------------------
    # External Integration Projection
    # --------------------------------------------------

    def _external_integration_projection(
        self,
        evidence,
        external_evidence=None,
    ):
        """
        Produce the canonical external integration state.

        State semantics:

            NOT_REQUESTED
                Integration was not requested.

            CONNECTED_WITH_EVIDENCE
                Integration succeeded and evidence was returned.

            CONNECTED_NO_EVIDENCE
                Integration succeeded but no evidence was returned.

            AUTHENTICATION_FAILED
            PERMISSION_DENIED
            RATE_LIMITED
            NETWORK_ERROR
            REPOSITORY_UNAVAILABLE
            INVALID_REPOSITORY
                Integration was requested but failed.

        This method deliberately keeps integration status separate
        from the actual evidence list.
        """

        # --------------------------------------------------
        # Default state
        # --------------------------------------------------

        integration = {

            "requested":
                False,

            "connected":
                False,

            "status":
                "NOT_REQUESTED",

            "providers":
                [],

            "evidence_count":
                0,

        }

        # --------------------------------------------------
        # Integration not requested
        # --------------------------------------------------

        if external_evidence is None:
            return integration

        integration["requested"] = True

        # --------------------------------------------------
        # Prefer explicit collector-provided canonical state
        # when available.
        # --------------------------------------------------

        collector_integration = {}

        if isinstance(
            evidence,
            dict,
        ):

            candidate = evidence.get(
                "external_integration"
            )

            if isinstance(
                candidate,
                dict,
            ):

                collector_integration = candidate

        # --------------------------------------------------
        # Provider
        # --------------------------------------------------

        providers = (
            collector_integration.get(
                "providers"
            )
            if collector_integration
            else None
        )

        if not isinstance(
            providers,
            list,
        ):

            providers = []

        # --------------------------------------------------
        # Fall back to the external provider itself.
        # --------------------------------------------------

        if not providers:

            provider = None

            if isinstance(
                external_evidence,
                dict,
            ):

                provider = (
                    external_evidence.get(
                        "source"
                    )
                    or external_evidence.get(
                        "provider"
                    )
                    or external_evidence.get(
                        "external_provider"
                    )
                )

            if provider:
                providers = [
                    str(provider)
                ]

        # --------------------------------------------------
        # Preserve collector-level provider metadata too.
        # --------------------------------------------------

        if not providers and isinstance(
            evidence,
            dict,
        ):

            provenance = evidence.get(
                "provenance",
                {},
            )

            if isinstance(
                provenance,
                dict,
            ):

                existing = provenance.get(
                    "external_providers",
                    [],
                )

                if isinstance(
                    existing,
                    list,
                ):

                    providers = [
                        str(item)
                        for item in existing
                        if item
                    ]

        # --------------------------------------------------
        # Status
        # --------------------------------------------------

        status = (
            collector_integration.get(
                "status"
            )
            if collector_integration
            else None
        )

        if not status and isinstance(
            external_evidence,
            dict,
        ):

            status = external_evidence.get(
                "status"
            )

        # --------------------------------------------------
        # Legacy collector fallback.
        # --------------------------------------------------

        if not status and isinstance(
            evidence,
            dict,
        ):

            status = evidence.get(
                "external_status"
            )

        if not status:
            status = "UNKNOWN"

        # --------------------------------------------------
        # Connected
        # --------------------------------------------------

        connected = (
            collector_integration.get(
                "connected"
            )
            if collector_integration
            else None
        )

        if connected is None and isinstance(
            external_evidence,
            dict,
        ):

            connected = external_evidence.get(
                "connected"
            )

        if connected is None:

            connected = str(
                status
            ).startswith(
                "CONNECTED_"
            )

        # --------------------------------------------------
        # Evidence count
        # --------------------------------------------------

        evidence_count = (
            collector_integration.get(
                "evidence_count"
            )
            if collector_integration
            else None
        )

        if evidence_count is None and isinstance(
            external_evidence,
            dict,
        ):

            evidence_count = (
                external_evidence.get(
                    "evidence_count"
                )
            )

        if evidence_count is None and isinstance(
            evidence,
            dict,
        ):

            counts = evidence.get(
                "counts",
                {},
            )

            if isinstance(
                counts,
                dict,
            ):

                evidence_count = counts.get(
                    "external",
                    0,
                )

        try:

            evidence_count = max(
                0,
                int(
                    evidence_count
                    if evidence_count is not None
                    else 0
                ),
            )

        except (
            TypeError,
            ValueError,
        ):

            evidence_count = 0

        return {

            "requested":
                True,

            "connected":
                bool(
                    connected
                ),

            "status":
                str(
                    status
                ),

            "providers":
                list(
                    dict.fromkeys(
                        providers
                    )
                ),

            "evidence_count":
                evidence_count,

        }

    # --------------------------------------------------
    # External Evidence Helpers
    # --------------------------------------------------

    @staticmethod
    def _external_binding_projection(
        evidence,
        external_evidence=None,
    ):
        """
        Project an explicitly supplied external engineering binding.

        A binding identifies an external artifact. It does not assert
        causality, success, or outcome.
        """

        candidates = []

        if isinstance(external_evidence, dict):
            candidate = external_evidence.get("binding")
            if isinstance(candidate, dict):
                candidates.append(candidate)

        if isinstance(evidence, dict):
            candidate = evidence.get("external_binding")
            if isinstance(candidate, dict):
                candidates.append(candidate)

            provenance = evidence.get("provenance", {})
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

    def _external_evidence_items(
        self,
        evidence,
    ):
        """
        Return the actual external evidence items.

        This deliberately does not use integration status.
        """

        if not isinstance(
            evidence,
            dict,
        ):
            return []

        external = evidence.get(
            "evidence",
            {},
        )

        if not isinstance(
            external,
            dict,
        ):
            return []

        items = external.get(
            "external",
            [],
        )

        if not isinstance(
            items,
            list,
        ):
            return []

        return items

    def _external_providers(
        self,
        evidence,
        external_evidence=None,
    ):
        """
        Return normalized provider names.

        This is compatibility metadata.
        The canonical integration object is still
        provenance.external_integration.
        """

        providers = []

        # --------------------------------------------------
        # Collector provenance
        # --------------------------------------------------

        if isinstance(
            evidence,
            dict,
        ):

            provenance = evidence.get(
                "provenance",
                {},
            )

            if isinstance(
                provenance,
                dict,
            ):

                values = provenance.get(
                    "external_providers",
                    [],
                )

                if isinstance(
                    values,
                    list,
                ):

                    providers.extend(
                        values
                    )

        # --------------------------------------------------
        # Collector integration object
        # --------------------------------------------------

        if isinstance(
            evidence,
            dict,
        ):

            integration = evidence.get(
                "external_integration",
                {},
            )

            if isinstance(
                integration,
                dict,
            ):

                values = integration.get(
                    "providers",
                    [],
                )

                if isinstance(
                    values,
                    list,
                ):

                    providers.extend(
                        values
                    )

        # --------------------------------------------------
        # Direct external adapter result
        # --------------------------------------------------

        if isinstance(
            external_evidence,
            dict,
        ):

            provider = (
                external_evidence.get(
                    "source"
                )
                or external_evidence.get(
                    "provider"
                )
                or external_evidence.get(
                    "external_provider"
                )
            )

            if provider:
                providers.append(
                    provider
                )

        return list(
            dict.fromkeys(
                str(item)
                for item in providers
                if item
            )
        )

    # --------------------------------------------------
    # Knowledge Projection
    # --------------------------------------------------

    def _knowledge_projection(
        self,
        decision,
        repository_plan,
        evidence,
        external_integration=None,
    ):
        """
        Produce the useful developer-facing interpretation
        without manufacturing engineering facts.
        """

        selected_goal = self._get(
            decision,
            "selected_goal",
        )

        canonical_decision = self._get(
            decision,
            "decision",
        )

        decision_reason = self._get(
            decision,
            "decision_reason",
        )

        strategy = self._get(
            repository_plan,
            "engineering_strategy",
        )

        objective = self._get(
            repository_plan,
            "objective",
        )

        expected_result = self._get(
            repository_plan,
            "expected_result",
        )

        counts = (
            evidence.get(
                "counts",
                {},
            )
            if isinstance(
                evidence,
                dict,
            )
            else {}
        )

        if not isinstance(
            counts,
            dict,
        ):
            counts = {}

        # --------------------------------------------------
        # Preserve the canonical external state in knowledge
        # as a useful developer-facing projection.
        # --------------------------------------------------

        if not isinstance(
            external_integration,
            dict,
        ):

            external_integration = (
                self._external_integration_projection(
                    evidence=evidence,
                    external_evidence=None,
                )
            )

        return {

            "current_goal":
                selected_goal,

            "current_decision":
                canonical_decision,

            "decision_rationale":
                (
                    decision_reason
                    if decision_reason
                    else "UNKNOWN"
                ),

            "engineering_strategy":
                strategy
                if strategy
                else "UNKNOWN",

            "current_objective":
                objective
                if objective
                else "UNKNOWN",

            "expected_result":
                expected_result
                if expected_result
                else "UNKNOWN",

            "evidence_summary": {

                "direct":
                    counts.get(
                        "direct",
                        0,
                    ),

                "related":
                    counts.get(
                        "related",
                        0,
                    ),

                "context":
                    counts.get(
                        "context",
                        0,
                    ),

                "unknown":
                    counts.get(
                        "unknown",
                        0,
                    ),

                "external":
                    counts.get(
                        "external",
                        0,
                    ),

            },

            "external_integration":
                external_integration,

            "outcome":
                "UNKNOWN",

            "decision_validity":
                "UNKNOWN",

            "decision_confidence":
                self._get(
                    decision,
                    "confidence",
                ),

        }

    # --------------------------------------------------
    # Unknowns
    # --------------------------------------------------

    def _unknowns(
        self,
        decision,
        repository_plan,
        evidence,
    ):
        """
        Explicitly surface knowledge gaps.

        Unknown is a valid state and is preferable to fabricated
        engineering knowledge.
        """

        unknowns = []

        if not self._get(
            decision,
            "decision_reason",
        ):

            unknowns.append(
                "Explicit decision rationale is unavailable."
            )

        if repository_plan is None:

            unknowns.append(
                "Canonical RepositoryPlan was not supplied."
            )

        if not self._get(
            repository_plan,
            "expected_result",
        ):

            unknowns.append(
                "Canonical expected result is unavailable."
            )

        evidence_counts = (
            evidence.get(
                "counts",
                {},
            )
            if isinstance(
                evidence,
                dict,
            )
            else {}
        )

        if (
            evidence_counts.get(
                "direct",
                0,
            ) == 0
        ):

            unknowns.append(
                (
                    "No directly matching repository evidence "
                    "was found for the current decision."
                )
            )

        if not self._has_explicit_outcome(
            evidence
        ):

            unknowns.append(
                (
                    "No verified engineering outcome is "
                    "present in the collected repository evidence."
                )
            )

        # --------------------------------------------------
        # External integration gaps
        #
        # Do not report "no evidence" as an error.
        # CONNECTED_NO_EVIDENCE is a valid state.
        # --------------------------------------------------

        external_integration = (
            self._external_integration_projection(
                evidence=evidence,
                external_evidence=None,
            )
        )

        if (
            external_integration.get(
                "requested"
            )
            and
            not external_integration.get(
                "connected"
            )
        ):

            status = external_integration.get(
                "status",
                "UNKNOWN",
            )

            unknowns.append(
                (
                    "External evidence integration was requested "
                    f"but was not connected: {status}."
                )
            )

        if not unknowns:

            unknowns.append(
                "No additional provenance gaps detected."
            )

        return unknowns

    # --------------------------------------------------
    # Canonical Decision
    # --------------------------------------------------

    def _decision_projection(
        self,
        decision,
    ):

        return {

            "repository":
                self._safe_value(
                    self._get(
                        decision,
                        "repository",
                    )
                ),

            "selected_goal":
                self._safe_value(
                    self._get(
                        decision,
                        "selected_goal",
                    )
                ),

            "decision":
                self._safe_value(
                    self._get(
                        decision,
                        "decision",
                    )
                ),

            "decision_reason":
                self._safe_value(
                    self._get(
                        decision,
                        "decision_reason",
                    )
                ),

            "priority":
                self._safe_value(
                    self._get(
                        decision,
                        "priority",
                    )
                ),

            "confidence":
                self._safe_value(
                    self._get(
                        decision,
                        "confidence",
                    )
                ),

            "strategic_focus":
                self._safe_value(
                    self._get(
                        decision,
                        "strategic_focus",
                    )
                ),

            "dominant_risk":
                self._safe_value(
                    self._get(
                        decision,
                        "dominant_risk",
                    )
                ),

            "recommended_next_step":
                self._safe_value(
                    self._get(
                        decision,
                        "recommended_next_step",
                    )
                ),

            "policy_action":
                self._safe_value(
                    self._get(
                        decision,
                        "policy_action",
                    )
                ),

        }

    # --------------------------------------------------
    # Canonical Plan
    # --------------------------------------------------

    def _plan_projection(
        self,
        repository_plan,
    ):

        if repository_plan is None:

            return {

                "available":
                    False,

                "reason":
                    "No canonical RepositoryPlan was supplied.",

            }

        sprints = (
            self._get(
                repository_plan,
                "sprints",
                [],
            )
            or []
        )

        normalized_sprints = []

        for sprint in sprints:

            if not isinstance(
                sprint,
                dict,
            ):
                continue

            tasks = []

            for task in (
                sprint.get(
                    "tasks",
                    [],
                )
                or []
            ):

                if (
                    isinstance(
                        task,
                        str,
                    )
                    and
                    task.strip()
                ):

                    tasks.append(
                        task.strip()
                    )

            normalized_sprints.append({

                "name":
                    sprint.get(
                        "name"
                    ),

                "priority":
                    sprint.get(
                        "priority"
                    ),

                "tasks":
                    tasks,

            })

        return {

            "available":
                True,

            "repository":
                self._safe_value(
                    self._get(
                        repository_plan,
                        "repository",
                    )
                ),

            "decision":
                self._safe_value(
                    self._get(
                        repository_plan,
                        "decision",
                    )
                ),

            "objective":
                self._safe_value(
                    self._get(
                        repository_plan,
                        "objective",
                    )
                ),

            "engineering_strategy":
                self._safe_value(
                    self._get(
                        repository_plan,
                        "engineering_strategy",
                    )
                ),

            "expected_result":
                self._safe_value(
                    self._get(
                        repository_plan,
                        "expected_result",
                    )
                ),

            "priority":
                self._safe_value(
                    self._get(
                        repository_plan,
                        "priority",
                    )
                ),

            "confidence":
                self._safe_value(
                    self._get(
                        repository_plan,
                        "confidence",
                    )
                ),

            "sprints":
                normalized_sprints,

        }

    # --------------------------------------------------
    # Outcome Detection
    # --------------------------------------------------

    @staticmethod
    def _has_explicit_outcome(
        evidence,
    ):
        """
        Deliberately conservative.

        Current repository evidence does not become an outcome
        merely because commits or files exist.

        A future CI/outcome collector can populate this field.
        """

        if not isinstance(
            evidence,
            dict,
        ):

            return False

        explicit_outcome = (
            evidence.get(
                "outcome",
            )
        )

        return bool(
            explicit_outcome
        )

    # --------------------------------------------------
    # Generic Helpers
    # --------------------------------------------------

    @staticmethod
    def _get(
        value,
        field,
        default=None,
    ):

        if value is None:
            return default

        if isinstance(
            value,
            dict,
        ):

            return value.get(
                field,
                default,
            )

        return getattr(
            value,
            field,
            default,
        )

    def _safe_value(
        self,
        value,
    ):

        if value is None:
            return None

        if isinstance(
            value,
            dict,
        ):

            return {
                str(key):
                    self._safe_value(
                        item
                    )

                for key, item
                in value.items()
            }

        if isinstance(
            value,
            list,
        ):

            return [
                self._safe_value(
                    item
                )

                for item
                in value
            ]

        if isinstance(
            value,
            tuple,
        ):

            return [
                self._safe_value(
                    item
                )

                for item
                in value
            ]

        if isinstance(
            value,
            (
                str,
                int,
                float,
                bool,
            ),
        ):

            return value

        isoformat = getattr(
            value,
            "isoformat",
            None,
        )

        if callable(
            isoformat
        ):

            try:
                return isoformat()

            except Exception:
                pass

        return str(
            value
        )