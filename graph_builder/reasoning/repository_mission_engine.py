"""
Graphify

Phase 13

Stage P13.1

Repository Mission Engine

Builds the engineering mission
from repository identity.

Author:
Graphify Core
"""

from graph_builder.cognition.repository_mission import (
    RepositoryMission,
)


class RepositoryMissionEngine:

    VERSION = "P13.1"

    # ------------------------------------------

    def build(self, identity):

        engineering_identity = identity.identity

        mission = self._infer_mission(
            engineering_identity
        )

        scope = self._engineering_scope(
            engineering_identity
        )

        confidence = self._confidence(
            engineering_identity
        )

        return RepositoryMission(

            repository=identity.repository,

            identity=engineering_identity,

            mission=mission,

            engineering_scope=scope,

            confidence=confidence,

        )

    # ------------------------------------------

    def _infer_mission(self, identity):

        mapping = {

            "Autonomous Engineering Brain":
            (
                "Continuously understand, "
                "reason about, improve, "
                "and autonomously evolve "
                "software repositories."
            ),

            "Engineering Automation Platform":
            (
                "Automate engineering "
                "workflows while preserving "
                "software quality."
            ),

            "Repository Intelligence Platform":
            (
                "Generate engineering "
                "knowledge from software "
                "repositories."
            ),

            "General Software Repository":
            (
                "Provide reusable software "
                "engineering functionality."
            ),

        }

        return mapping.get(

            identity,

            "Support software engineering.",

        )

    # ------------------------------------------

    def _engineering_scope(self, identity):

        if "Engineering" in identity:

            return "Repository Engineering"

        if "Repository" in identity:

            return "Repository Intelligence"

        return "Software Engineering"

    # ------------------------------------------

    def _confidence(self, identity):

        if identity == "Autonomous Engineering Brain":

            return 0.97

        return 0.90