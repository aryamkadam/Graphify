"""
Graphify

Phase 15

Stage P15.3

Repository Cognitive Reasoning Engine

Author:
Graphify Core
"""

from graph_builder.reasoning.repository_cognitive_reasoning import (
    RepositoryCognitiveReasoning,
)


class RepositoryCognitiveReasoningEngine:

    VERSION = "P15.3"

    # ---------------------------------------------

    def build(

        self,

        insight,

    ):

        conclusions = []

        if (

            insight.dominant_focus

            == "Reduce Technical Debt"

        ):

            conclusions.append(

                "Technical debt is currently the highest engineering priority."

            )

        if (

            insight.engineering_direction

            == "Repository Evolution"

        ):

            conclusions.append(

                "Repository architecture is suitable for continuous evolution."

            )

        if (

            insight.evolution_readiness

            == "HIGH"

        ):

            conclusions.append(

                "Repository is ready for autonomous engineering planning."

            )

        if (

            "Autonomous Engineering"

            in insight.biggest_strength

        ):

            conclusions.append(

                "Current engineering strategy aligns with repository mission."

            )

        return RepositoryCognitiveReasoning(

            repository=insight.repository,

            engineering_conclusions=conclusions,

            dominant_reasoning=self._reasoning(

                insight,

            ),

            repository_state=self._state(

                insight,

            ),

            engineering_maturity=self._maturity(

                insight,

            ),

            confidence=insight.confidence,

        )

    # ---------------------------------------------

    def _reasoning(

        self,

        insight,

    ):

        if (

            insight.engineering_direction

            == "Repository Evolution"

        ):

            return "Architecture Evolution"

        return "General Engineering"

    # ---------------------------------------------

    def _state(

        self,

        insight,

    ):

        if (

            insight.evolution_readiness

            == "HIGH"

        ):

            return "Healthy"

        return "Needs Improvement"

    # ---------------------------------------------

    def _maturity(

        self,

        insight,

    ):

        if insight.confidence >= 0.95:

            return "HIGH"

        if insight.confidence >= 0.85:

            return "MEDIUM"

        return "LOW"

    # ---------------------------------------------

    def status(self):

        return {

            "engine":

            "Repository Cognitive Reasoning Engine",

            "version": self.VERSION,

        }