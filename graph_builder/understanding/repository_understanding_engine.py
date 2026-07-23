"""
Graphify

Phase 15

Stage P15.1

Repository Understanding Engine

Builds Graphify's semantic understanding
of a repository from repository intelligence.

Author:
Graphify Core
"""

from graph_builder.understanding.repository_understanding import (
    RepositoryUnderstanding,
)


class RepositoryUnderstandingEngine:

    VERSION = "P15.1"

    # --------------------------------------------------

    def build_understanding(

        self,

        repository,

        identity,

        mission,

        goals,

    ):

        understanding = RepositoryUnderstanding(

            repository=repository,

            identity=identity.identity,

            mission=mission.mission,

            goals=goals.goals,

            engineering_scope=identity.engineering_type,

            current_focus=self._current_focus(goals),

            architecture_summary=self._architecture_summary(identity),

            strengths=[],

            weaknesses=[],

            technical_debt=[],

            architectural_risks=[],

            evolution_opportunities=[],

            confidence=min(

                identity.confidence,

                mission.confidence,

                goals.confidence,

            ),

        )

        return understanding

    # --------------------------------------------------

    def _current_focus(

        self,

        goals,

    ):

        if goals.goals:

            return goals.goals[0]

        return "Repository Evolution"

    # --------------------------------------------------

    def _architecture_summary(

        self,

        identity,

    ):

        if identity.engineering_type == "Engineering AI":

            return (

                "Repository is evolving as an autonomous engineering system."

            )

        elif identity.engineering_type == "Repository Intelligence":

            return (

                "Repository focuses on repository intelligence."

            )

        elif identity.engineering_type == "Automation":

            return (

                "Repository focuses on engineering automation."

            )

        return (

            "General software repository."

        )

    # --------------------------------------------------

    def status(self):

        return {

            "version": self.VERSION,

            "engine": "Repository Understanding Engine",

            "typed_models": True,

        }