"""
Graphify

Phase 15

Stage P15.2

Repository Insight Engine

Author:
Graphify Core
"""

from graph_builder.understanding.repository_insight import (
    RepositoryInsight,
)


class RepositoryInsightEngine:

    VERSION = "P15.2"

    # --------------------------------------------------

    def build(

        self,

        understanding,

    ):

        return RepositoryInsight(

            repository=understanding.repository,

            dominant_focus=understanding.current_focus,

            biggest_strength=self._strength(understanding),

            biggest_weakness=self._weakness(understanding),

            highest_priority_goal=understanding.goals[0],

            engineering_direction=self._direction(understanding),

            architectural_state=understanding.architecture_summary,

            evolution_readiness=self._readiness(understanding),

            confidence=understanding.confidence,

        )

    # --------------------------------------------------

    def _strength(

        self,

        understanding,

    ):

        if "Autonomous Engineering" in understanding.identity:

            return "Autonomous Engineering Vision"

        return "Repository Intelligence"

    # --------------------------------------------------

    def _weakness(

        self,

        understanding,

    ):

        if understanding.weaknesses:

            return understanding.weaknesses[0]

        return "Strength analysis unavailable"

    # --------------------------------------------------

    def _direction(

        self,

        understanding,

    ):

        if "Repository Evolution" in understanding.goals:

            return "Repository Evolution"

        return "Architecture Improvement"

    # --------------------------------------------------

    def _readiness(

        self,

        understanding,

    ):

        if understanding.confidence >= 0.95:

            return "HIGH"

        if understanding.confidence >= 0.85:

            return "MEDIUM"

        return "LOW"

    # --------------------------------------------------

    def status(self):

        return {

            "engine": "Repository Insight Engine",

            "version": self.VERSION,

        }