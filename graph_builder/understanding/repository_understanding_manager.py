"""
Graphify

Phase 22

Stage P22.7

Repository Understanding Manager

Acts as the single entry point for Repository
Understanding inside Graphify.

Responsibilities

• Own Repository Understanding Engine
• Build Repository Understanding
• Cache latest understanding
• Expose understanding API

The manager NEVER performs reasoning.

Author:
Graphify Core
"""

from graph_builder.understanding.repository_understanding_engine import (
    RepositoryUnderstandingEngine,
)


class RepositoryUnderstandingManager:

    VERSION = "P22.7"

    # --------------------------------------------------

    def __init__(

        self,

        repository_context,

    ):

        self.context = repository_context

        self.engine = RepositoryUnderstandingEngine(

            repository_context,

        )

        self._latest_understanding = None

    # --------------------------------------------------

    def build(self):
        """
        Build repository understanding.
        """

        self._latest_understanding = self.engine.build()

        return self._latest_understanding

    # --------------------------------------------------

    def latest(self):
        """
        Return latest repository understanding.
        """

        return self._latest_understanding

    # --------------------------------------------------

    def clear(self):
        """
        Clear cached understanding.
        """

        self._latest_understanding = None

    # --------------------------------------------------

    def is_available(self):

        return self._latest_understanding is not None

    # --------------------------------------------------

    def status(self):

        return {

            "manager": "READY",

            "understanding_available":

                self.is_available(),

            "version":

                self.VERSION,

        }