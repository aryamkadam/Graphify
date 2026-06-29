"""
Stage 18.1

Repository Strategy Engine

The Strategy Engine converts repository intelligence
into an engineering strategy.

Instead of explaining what happened, it decides
the best overall direction for the repository.
"""


class RepositoryStrategyEngine:

    def build(

        self,

        consciousness,

        knowledge,

        experience,

    ):

        phase = consciousness.get(
            "repository_identity",
            {}
        ).get(
            "phase",
            "Unknown"
        )

        direction = consciousness.get(
            "repository_identity",
            {}
        ).get(
            "technical_direction",
            "Unknown"
        )

        experience_level = experience.get(
            "experience_level",
            "Unknown"
        )

        confidence = knowledge.get(
            "knowledge_confidence",
            0.5
        )

        strategy = self._decide_strategy(

            phase,

            direction,

            experience_level,

            confidence,

        )

        return {

            "repository_phase": phase,

            "technical_direction": direction,

            "experience_level": experience_level,

            "knowledge_confidence": confidence,

            "engineering_strategy": strategy,

            "summary": (

                f"The recommended engineering strategy "

                f"is '{strategy}'."

            )

        }

    # -----------------------------------------

    def _decide_strategy(

        self,

        phase,

        direction,

        experience,

        confidence,

    ):

        if phase == "Stabilization":

            return "Repository-wide Refactoring"

        if phase == "Expansion":

            return "Controlled Feature Expansion"

        if phase == "Recovery":

            return "Aggressive Technical Debt Reduction"

        if direction == "Positive":

            return "Continuous Engineering Improvement"

        if direction == "Negative":

            return "Repository Recovery Plan"

        return "Monitor Repository Evolution"