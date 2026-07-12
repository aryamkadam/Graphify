"""
Graphify

Phase 3

Stage P3.10

Engineering Sprint

Represents one completed engineering sprint.

Author:
Graphify Core
"""

from datetime import datetime


class EngineeringSprint:

    VERSION = "P3.10"

    def __init__(

        self,

        objective,

        strategy,

        report,

    ):

        self.objective = objective

        self.strategy = strategy

        self.report = report

        self.created_at = datetime.now()

    # --------------------------------------------------

    def summary(self):

        return {

            "objective": self.objective,

            "strategy": self.strategy,

            "tasks_completed":

                self.report["completed_tasks"],

            "timestamp":

                self.created_at.isoformat(),

            "version":

                self.VERSION,

        }

    # --------------------------------------------------

    def details(self):

        return {

            "objective": self.objective,

            "strategy": self.strategy,

            "report": self.report,

            "timestamp":

                self.created_at.isoformat(),

            "version":

                self.VERSION,

        }