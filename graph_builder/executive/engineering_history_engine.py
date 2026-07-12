"""
Graphify

Phase 3

Stage P3.10

Engineering History Engine

Stores every completed engineering sprint.

Author:
Graphify Core
"""


class EngineeringHistoryEngine:

    VERSION = "P3.10"

    def __init__(self):

        self._history = []

    # --------------------------------------------------

    def archive(

        self,

        sprint,

    ):

        self._history.append(

            sprint

        )

    # --------------------------------------------------

    def latest(self):

        if not self._history:

            return None

        return self._history[-1]

    # --------------------------------------------------

    def all(self):

        return self._history

    # --------------------------------------------------

    def status(self):

        return {

            "sprints":

                len(self._history),

            "version":

                self.VERSION,

        }