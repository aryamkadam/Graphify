"""
Graphify

Phase 38
Stage 38.4 / 38.5

Engineering Decision Provenance

38.4:
    Canonical decision/plan provenance projection.

38.5:
    Automatic repository evidence collection.

This component remains READ-ONLY.

Canonical ownership remains external.
"""

from __future__ import annotations

import hashlib
from pathlib import Path

from graph_builder.provenance.decision_evidence_collector import (
    DecisionEvidenceCollector,
)


class EngineeringDecisionProvenance:

    VERSION = "38.5"

    STATUS = "EVIDENCE_ONLY"

    def __init__(
        self,
    ):

        self._evidence_collector = (
            DecisionEvidenceCollector()
        )

    # --------------------------------------------------
    # Public API
    # --------------------------------------------------

    def build(
        self,
        repository_path,
        decision,
        repository_plan=None,
    ):
        """
        Build a read-only engineering provenance record.

        Decision meaning always comes from the supplied canonical
        decision.

        Plan meaning always comes from the supplied canonical plan.

        Evidence comes from DecisionEvidenceCollector.

        No new engineering authority is introduced.
        """

        repository = (
            Path(
                repository_path
            ).resolve()
        )

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

        evidence = (
            self._evidence_collector.collect(

                repository_path=
                    repository,

                decision=
                    decision,

                repository_plan=
                    repository_plan,

            )
        )

        return {

            "record_version":
                self.VERSION,

            "status":
                self.STATUS,

            "repository":
                repository.name,

            "repository_path":
                str(repository),

            "decision":
                decision_projection,

            "plan":
                plan_projection,

            "evidence":
                evidence,

            "provenance": {

                "source":
                    (
                        "Graphify canonical decision, "
                        "canonical repository plan, and "
                        "directly observed repository evidence"
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

            "rationale_policy":
                (
                    "Rationale is preserved only when it already "
                    "exists in canonical decision state or is "
                    "explicitly supported by repository evidence. "
                    "The provenance system never invents rationale."
                ),

            "causality_policy":
                (
                    "Temporal or textual correlation is not treated "
                    "as proof that a repository change was caused by "
                    "the canonical decision."
                ),

        }

    # --------------------------------------------------
    # Canonical Decision Projection
    # --------------------------------------------------

    def _decision_projection(
        self,
        decision,
    ):

        return {

            "repository":
                self._get(
                    decision,
                    "repository",
                ),

            "selected_goal":
                self._get(
                    decision,
                    "selected_goal",
                ),

            "decision":
                self._get(
                    decision,
                    "decision",
                ),

            "decision_reason":
                self._get(
                    decision,
                    "decision_reason",
                ),

            "strategic_focus":
                self._get(
                    decision,
                    "strategic_focus",
                ),

            "policy_action":
                self._get(
                    decision,
                    "policy_action",
                ),

            "dominant_risk":
                self._get(
                    decision,
                    "dominant_risk",
                ),

            "priority":
                self._get(
                    decision,
                    "priority",
                ),

            "confidence":
                self._get(
                    decision,
                    "confidence",
                ),

            "engineering_evidence":
                self._safe_value(
                    self._get(
                        decision,
                        "engineering_evidence",
                    )
                ),

        }

    # --------------------------------------------------
    # Canonical Plan Projection
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

                if isinstance(
                    task,
                    str,
                ) and task.strip():

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
                self._get(
                    repository_plan,
                    "repository",
                ),

            "objective":
                self._get(
                    repository_plan,
                    "objective",
                ),

            "decision":
                self._get(
                    repository_plan,
                    "decision",
                ),

            "engineering_strategy":
                self._get(
                    repository_plan,
                    "engineering_strategy",
                ),

            "expected_result":
                self._get(
                    repository_plan,
                    "expected_result",
                ),

            "priority":
                self._get(
                    repository_plan,
                    "priority",
                ),

            "confidence":
                self._get(
                    repository_plan,
                    "confidence",
                ),

            "sprints":
                normalized_sprints,

        }

    # --------------------------------------------------
    # Helpers
    # --------------------------------------------------

    @staticmethod
    def _get(
        value,
        field,
        default=None,
    ):

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

    @staticmethod
    def _sha256(
        path,
    ):

        digest = hashlib.sha256()

        with path.open(
            "rb"
        ) as file:

            while True:

                chunk = file.read(
                    1024 * 1024
                )

                if not chunk:
                    break

                digest.update(
                    chunk
                )

        return digest.hexdigest()