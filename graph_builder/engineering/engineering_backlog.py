"""
Graphify

Stage 32.0

Engineering Backlog

Central engineering work queue
for Graphify.

Author:
Graphify Core
"""

from graph_builder.workers.engineering_task import EngineeringTask


class EngineeringBacklog:

    VERSION = "32.0"

    def __init__(self):

        self._tasks = []

    # --------------------------------------------------

    def add_task(

        self,

        title,

        description,

        priority="MEDIUM",

    ):

        task = EngineeringTask(

            title=title,

            description=description,

            priority=priority,

        )

        self._tasks.append(task)

        return task

    # --------------------------------------------------

    def tasks(self):

        return self._tasks

    # --------------------------------------------------

    def pending(self):

        return [

            task

            for task in self._tasks

            if task.status == "PENDING"

        ]

    # --------------------------------------------------

    def completed(self):

        return [

            task

            for task in self._tasks

            if task.status == "COMPLETED"

        ]

    # --------------------------------------------------

    def next_task(self):

        priority_order = {

            "HIGH": 0,

            "MEDIUM": 1,

            "LOW": 2,

        }

        pending = self.pending()

        if not pending:

            return None

        pending.sort(

            key=lambda task: priority_order.get(

                task.priority,

                99,

            )

        )

        return pending[0]

    # --------------------------------------------------

    def status(self):

        return {

            "version": self.VERSION,

            "total_tasks": len(self._tasks),

            "pending": len(self.pending()),

            "completed": len(self.completed()),

        }