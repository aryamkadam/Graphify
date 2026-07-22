"""
Graphify

Phase 13

Stage P13.2

Repository Goal

Represents the engineering goals
derived from the repository mission.

Author:
Graphify Core
"""

from dataclasses import dataclass


@dataclass(slots=True)
class RepositoryGoal:

    VERSION = "P13.2"

    repository: str

    mission: str

    goals: list[str]

    priority: str

    confidence: float

    # ------------------------------------------

    def summary(self):

        return {

            "repository": self.repository,

            "goal_count": len(self.goals),

            "priority": self.priority,

            "confidence": self.confidence,

            "version": self.VERSION,

        }

    # ------------------------------------------

    def to_dict(self):

        return {

            "repository": self.repository,

            "mission": self.mission,

            "goals": self.goals,

            "priority": self.priority,

            "confidence": self.confidence,

            "version": self.VERSION,

        }