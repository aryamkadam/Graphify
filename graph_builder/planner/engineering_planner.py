"""
Graphify

Stage 34.0

Engineering Planner

Generates engineering work from
repository intelligence.

Author:
Graphify Core
"""

from graph_builder.engineering.engineering_backlog import (
    EngineeringBacklog,
)


class EngineeringPlanner:

    VERSION = "34.0"

    def __init__(self):

        self.backlog = EngineeringBacklog()

    # --------------------------------------------------

    def generate_plan(

        self,

        repository_brain,

    ):

        priority = repository_brain["priorities"]["highest_priority"]["task"]

        strategy = repository_brain["strategy"]["engineering_strategy"]

        self.backlog.add_task(

            title=priority,

            description=strategy,

            priority="HIGH",

        )

        return {

            "status": "success",

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