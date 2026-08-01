"""
Graphify

Stage 17.0.5

Repository History Manager

Owns repository evolution history.

Responsibilities:
- Store evolution reports
- Return repository history
- Provide a single source of truth for Stage 17

Future:
- Persistent storage
- Git-backed history
- Database history
- Cloud history

Author:
Graphify Core
"""


class RepositoryHistoryManager:

    VERSION = "P17.0.5"

    def __init__(self):

        self._history = []

    # --------------------------------------------------

    def append(self, evolution_report):

        if evolution_report:

            self._history.append(evolution_report)

    # --------------------------------------------------

    def get_history(self):

        return list(self._history)

    # --------------------------------------------------

    def latest(self):

        if not self._history:

            return None

        return self._history[-1]

    # --------------------------------------------------

    def clear(self):

        self._history.clear()

    # --------------------------------------------------

    def size(self):

        return len(self._history)