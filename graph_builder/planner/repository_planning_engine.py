"""
Graphify

Phase 17

Stage P17.0

Repository Planning Engine

Author:
Graphify Core
"""

from graph_builder.planning.repository_plan import (
    RepositoryPlan,
)


class RepositoryExecutionPlanningEngine:

    VERSION = "P17.0"

    # ------------------------------------------

    def build(

        self,

        decision,

    ):

        objective = self._objective(decision)

        strategy = self._strategy(decision)

        sprints = self._sprints(decision)

        workers = self._workers(decision)

        dependencies = self._dependencies()

        expected = self._expected_result()

        return RepositoryPlan(

            repository=decision.repository,

            decision=decision.decision,

            objective=objective,

            engineering_strategy=strategy,

            sprints=sprints,

            workers=workers,

            dependencies=dependencies,

            expected_result=expected,

            priority=decision.priority,

            confidence=decision.confidence,

        )

    # ------------------------------------------

    def _objective(self, decision):

        if decision.selected_goal == "Reduce Technical Debt":

            return "Reduce Technical Debt"

        return "Repository Evolution"

    # ------------------------------------------

    def _strategy(self, decision):

        if decision.selected_goal == "Reduce Technical Debt":

            return "Repository-wide Refactoring"

        return "Continuous Repository Evolution"

    # ------------------------------------------

    def _sprints(self, decision):

        if decision.selected_goal == "Reduce Technical Debt":

            return [

                {

                    "name": "Sprint 1",

                    "tasks": [

                        "Detect Dead Code",

                        "Remove Dead Code",

                        "Improve Architecture",

                    ],

                },

                {

                    "name": "Sprint 2",

                    "tasks": [

                        "Run Tests",

                        "Validate Repository",

                    ],

                },

            ]

        return []

    # ------------------------------------------

    def _workers(self, decision):

        return [

            "Repository Architect",

            "Code Engineer",

            "Testing Engineer",

        ]

    # ------------------------------------------

    def _dependencies(self):

        return [

            "Detect Dead Code",

            "Remove Dead Code",

            "Improve Architecture",

            "Run Tests",

            "Validate Repository",

        ]

    # ------------------------------------------

    def _expected_result(self):

        return "Improved repository health and maintainability"

    # ------------------------------------------

    def status(self):

        return {

            "engine": "Repository Planning Engine",

            "version": self.VERSION,

        }