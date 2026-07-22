"""
Graphify

Phase 14

Stage P14.1

Execution Coordinator

Selects the next executable engineering task
from the Engineering Backlog.

This component NEVER executes work.

It only coordinates execution.

Author:
Graphify Core
"""


class ExecutionCoordinator:

    VERSION = "P14.1"

    def __init__(self, backlog):

        self.backlog = backlog

    # --------------------------------------------------

    def select_next_task(self):
        """
        Returns the next executable task.
        """

        task = self.backlog.next_task()

        if task is None:
            return None

        return task

    # --------------------------------------------------

    def validate_task(self, task):
        """
        Ensures the task is executable.
        """

        if task is None:
            return False

        if getattr(task, "status", None) != "PENDING":
            return False

        return True

    # --------------------------------------------------

    def execution_ready(self):
        """
        Returns the next validated task.
        """

        task = self.select_next_task()

        if not self.validate_task(task):
            return None

        return task

    # --------------------------------------------------

    def coordinator_status(self):

        return {

            "version": self.VERSION,

            "pending_tasks":
                self.backlog.status()["pending"],

            "ready":
                self.backlog.status()["pending"] > 0,

        }