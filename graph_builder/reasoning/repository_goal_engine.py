"""
Graphify

Phase 13

Stage P13.2

Repository Goal Engine

Generates engineering goals
from the repository mission.

Author:
Graphify Core
"""

from graph_builder.cognition.repository_goal import (
    RepositoryGoal,
)


class RepositoryGoalEngine:

    VERSION = "P13.2"

    # ------------------------------------------

    def build(self, mission):

        goals = self._infer_goals(
            mission.mission
        )

        priority = self._priority(goals)

        confidence = self._confidence(goals)

        return RepositoryGoal(

            repository=mission.repository,

            mission=mission.mission,

            goals=goals,

            priority=priority,

            confidence=confidence,

        )

    # ------------------------------------------

    def _infer_goals(self, mission_text):

        goals = []

        text = mission_text.lower()

        if "improve" in text:

            goals.extend([

                "Reduce Technical Debt",

                "Improve Architecture",

                "Increase Maintainability",

            ])

        if "understand" in text:

            goals.extend([

                "Expand Repository Knowledge",

                "Improve Repository Understanding",

            ])

        if "reason" in text:

            goals.extend([

                "Improve Engineering Decisions",

                "Increase Reasoning Accuracy",

            ])

        if "evolve" in text:

            goals.extend([

                "Continuous Learning",

                "Repository Evolution",

            ])

        return list(dict.fromkeys(goals))

    # ------------------------------------------

    def _priority(self, goals):

        if len(goals) >= 6:

            return "HIGH"

        if len(goals) >= 3:

            return "MEDIUM"

        return "LOW"

    # ------------------------------------------

    def _confidence(self, goals):

        return round(

            min(

                1.0,

                0.80 + len(goals) * 0.02,

            ),

            2,

        )