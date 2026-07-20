"""
Graphify

Phase 4.2

Engineering Sprint Generator

Converts engineering objectives into
structured sprint tasks.

Author:
Graphify Core
"""


class EngineeringSprintGenerator:

    VERSION = "P4.2"

    def __init__(self, objective_plan):

        self.plan = objective_plan

    # --------------------------------------------

    def _assign_role(self, objective):

        text = objective.lower()

        if "architecture" in text:

            return "architecture"

        if "runtime" in text:

            return "implementation"

        if "plugin" in text:

            return "implementation"

        if "worker" in text:

            return "testing"

        return "implementation"

    # --------------------------------------------

    def build(self):

        sprint_tasks = []

        objectives = self.plan.get(

            "objectives",

            [],

        )

        priority = self.plan.get(

            "priority",

            "MEDIUM",

        )

        strategy = self.plan.get(

            "strategy",

            "OPTIMIZATION",

        )

        for index, objective in enumerate(

            objectives,

            start=1,

        ):

            sprint_tasks.append(

                {

                    "id": index,

                    "title": objective,

                    "role": self._assign_role(

                        objective

                    ),

                    "priority": priority,

                    "status": "PENDING",

                }

            )

        return {

            "sprint": "Sprint-0001",

            "strategy": strategy,

            "priority": priority,

            "tasks": sprint_tasks,

            "version": self.VERSION,

        }