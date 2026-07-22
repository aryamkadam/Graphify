"""
Graphify

Phase 13

Stage P13.5

Engineering Planner

Transforms engineering decisions into
executable engineering plans.

Author:
Graphify Core
"""

from graph_builder.engineering.engineering_backlog import (
    EngineeringBacklog,
)


class EngineeringPlanner:

    VERSION = "P13.5"

    def __init__(self, decision_engine=None):

        self.backlog = EngineeringBacklog()

        # Future integration with Engineering Decision Engine
        self.decision_engine = decision_engine

    # --------------------------------------------------

    def generate_plan(
        self,
        repository_brain,
        engineering_decision=None,
    ):
        """
        Generates an engineering execution plan.

        Current compatibility:
            Uses repository_brain.

        Future architecture:
            Engineering Decision
                    ↓
            Engineering Planner
                    ↓
            Engineering Backlog
        """

        # --------------------------------------------
        # Future: Use Engineering Decision
        # --------------------------------------------

        if engineering_decision is not None:

            recommendation = engineering_decision.get(
                "recommendation",
                {}
            )

            priority = engineering_decision.get(
                "task",
                "Unknown Task"
            )

            strategy = recommendation.get(
                "strategy",
                "General Engineering Strategy"
            )

        # --------------------------------------------
        # Current compatibility
        # --------------------------------------------

        else:

            priority = repository_brain["priorities"][
                "highest_priority"
            ]["task"]

            strategy = repository_brain["strategy"][
                "engineering_strategy"
            ]

        # --------------------------------------------

        self.backlog.add_task(

            title=priority,

            description=strategy,

            priority="HIGH",

        )

        return {

            "status": "success",

            "planning_source":
                "Engineering Decision"
                if engineering_decision
                else "Repository Brain",

            "generated_tasks": 1,

            "strategy": strategy,

            "highest_priority": priority,

            "version": self.VERSION,

        }

    # --------------------------------------------------

    def backlog_status(self):

        return self.backlog.status()

    # --------------------------------------------------

    def next_task(self):

        task = self.backlog.next_task()

        if task:

            return task.to_dict()

        return None

    # --------------------------------------------------

    def planner_status(self):

        return {

            "version": self.VERSION,

            "decision_engine_available":
                self.decision_engine is not None,

            "backlog":
                self.backlog.status(),

        }