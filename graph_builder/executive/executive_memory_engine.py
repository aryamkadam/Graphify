"""
Graphify

Phase 5

Stage P5.6

Executive Memory Engine

Persistent executive memory for
Graphify's engineering leadership.

Stores only executive-level decisions,
not worker or runtime information.

Author:
Graphify Core
"""


class ExecutiveMemoryEngine:

    VERSION = "P5.6"

    def __init__(self):

        self._history = []

    # --------------------------------------------------

    def remember(

        self,

        executive_report,

    ):

        self._history.append(

            executive_report

        )

    # --------------------------------------------------

    def history(self):

        return list(

            self._history

        )

    # --------------------------------------------------

    def latest(self):

        if not self._history:

            return None

        return self._history[-1]

    # --------------------------------------------------

    def summary(self):

        if not self._history:

            return {

                "executive_decisions": 0,

                "latest_strategy": None,

                "version": self.VERSION,

            }

        latest = self.latest()

        return {

            "executive_decisions":

                len(self._history),

            "latest_strategy":

                latest.get(

                    "adaptation_strategy"

                ),

            "version":

                self.VERSION,

        }

    # --------------------------------------------------

    def export(self):

        """
        Portable executive brain.

        Future Cross-AI transfer
        will export this structure.
        """

        return {

            "executive_memory":

                self.history(),

            "summary":

                self.summary(),

            "version":

                self.VERSION,

        }