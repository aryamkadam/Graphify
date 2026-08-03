"""
Graphify

Phase 21

Stage P21.2

Repository Awareness Manager

Acts as the single entry point for Repository
Awareness inside Graphify.

Responsibilities

• Own Repository Awareness Engine
• Build Repository Awareness Report
• Cache latest awareness report
• Expose repository awareness API

The manager never performs awareness reasoning.

The manager delegates all awareness generation
to RepositoryAwarenessEngine.

Author:
Graphify Core
"""

from graph_builder.awareness.repository_awareness_engine import (
    RepositoryAwarenessEngine,
)


class RepositoryAwarenessManager:

    VERSION = "P21.2"

    # --------------------------------------------------

    def __init__(self, context):

        self.context = context

        self.engine = RepositoryAwarenessEngine(context)

        self._latest_report = None

    # --------------------------------------------------

    def build(self):
        """
        Build the latest awareness report.
        """

        self._latest_report = self.engine.build()

        return self._latest_report

    # --------------------------------------------------

    def latest(self):
        """
        Return the latest awareness report.
        """

        return self._latest_report

    # --------------------------------------------------

    def clear(self):
        """
        Clear cached awareness report.
        """

        self._latest_report = None

    # --------------------------------------------------

    def status(self):

        return {

            "manager": "READY",

            "report_available":

                self._latest_report is not None,

            "version":

                self.VERSION,

        }