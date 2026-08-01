"""
Graphify

Phase 9

Stage P9.6

Repository Learning Engine

Stores repository evolution history
for future engineering decisions.

Author:
Graphify Core
"""

from datetime import datetime


class RepositoryLearningStore:

    VERSION = "P9.6"

    def __init__(self):

        self._history = []

    # --------------------------------------------------

    def learn(self, evolution_report):

        record = {

            "timestamp": datetime.utcnow().isoformat() + "Z",

            "strategy": evolution_report.get("strategy"),

            "objective": evolution_report.get("objective"),

            "priority": evolution_report.get("priority"),

            "recommended_actions": evolution_report.get(
                "recommended_actions",
                [],
            ),

        }

        self._history.append(record)

        return {

            "stored_records": len(self._history),

            "latest_strategy": record["strategy"],

            "version": self.VERSION,

        }

    # --------------------------------------------------

    def history(self):

        return list(self._history)

    # --------------------------------------------------

    def latest(self):

        if not self._history:

            return None

        return self._history[-1]

    # --------------------------------------------------

    def summary(self):

        return {

            "repository_history": len(self._history),

            "latest_strategy": (
                self._history[-1]["strategy"]
                if self._history
                else None
            ),

            "version": self.VERSION,

        }