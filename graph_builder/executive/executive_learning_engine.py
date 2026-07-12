"""
Graphify

Stage 55.0

Executive Learning Engine

Uses engineering experience to improve
executive decisions.

Author:
Graphify Core
"""

from graph_builder.engineering.engineering_experience_engine import (
    EngineeringExperienceEngine,
)


class ExecutiveLearningEngine:

    VERSION = "55.0"

    def __init__(

        self,

        experience_engine: EngineeringExperienceEngine,

    ):

        self.experience_engine = experience_engine

    # --------------------------------------------------

    def decide(self):

        analysis = self.experience_engine.analyze()

        recommendations = analysis["recommendations"]

        if not recommendations:

            decision = "CONTINUE_CURRENT_STRATEGY"

        elif "Collect more engineering experience." in recommendations:

            decision = "COLLECT_EXPERIENCE"

        elif "Engineering knowledge graph is sparsely connected." in recommendations:

            decision = "STRENGTHEN_GRAPH"

        else:

            decision = "EXECUTIVE_REVIEW"

        return {

            "decision": decision,

            "recommendations": recommendations,

            "version": self.VERSION,

        }

    # --------------------------------------------------

    def summary(self):

        health = self.experience_engine.repository_health()

        return {

            "repository_health": health["health"],

            "version": self.VERSION,

        }