"""
Graphify

Phase 15

Stage P15.2

Repository Insight

Author:
Graphify Core
"""


class RepositoryInsight:

    VERSION = "P15.2"

    def __init__(

        self,

        repository,

        dominant_focus,

        biggest_strength,

        biggest_weakness,

        highest_priority_goal,

        engineering_direction,

        architectural_state,

        evolution_readiness,

        confidence,

    ):

        self.repository = repository

        self.dominant_focus = dominant_focus

        self.biggest_strength = biggest_strength

        self.biggest_weakness = biggest_weakness

        self.highest_priority_goal = highest_priority_goal

        self.engineering_direction = engineering_direction

        self.architectural_state = architectural_state

        self.evolution_readiness = evolution_readiness

        self.confidence = confidence

    # ---------------------------------------------

    def summary(self):

        return {

            "repository": self.repository,

            "dominant_focus": self.dominant_focus,

            "highest_priority_goal": self.highest_priority_goal,

            "engineering_direction": self.engineering_direction,

            "evolution_readiness": self.evolution_readiness,

            "confidence": self.confidence,

            "version": self.VERSION,

        }