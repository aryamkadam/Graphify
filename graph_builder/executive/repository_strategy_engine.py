"""
Graphify

Stage 18.1

Repository Strategy Engine

Transforms repository consciousness,
knowledge and experience into a
repository-wide engineering strategy.

This engine behaves like the executive
planning layer of Graphify.

Author:
Graphify Core
"""


class RepositoryStrategyEngine:

    VERSION = "P5.4"

    # --------------------------------------------------

    def build(

        self,

        consciousness,

        knowledge,

        experience,

    ):

        identity = consciousness.get(
            "repository_identity",
            {}
        )

        phase = identity.get(
            "phase",
            "Unknown"
        )

        direction = identity.get(
            "technical_direction",
            "Unknown"
        )

        experience_level = experience.get(
            "experience_level",
            "Unknown"
        )

        confidence = knowledge.get(
            "knowledge_confidence",
            0.50
        )

        strategy = self._decide_strategy(

            phase,

            direction,

            experience_level,

            confidence,

        )

        priority = self._priority(

            strategy

        )

        risk = self._risk(

            confidence,

            experience_level,

        )

        next_step = self._next_step(

            strategy

        )

        reasoning = self._reasoning(

            phase,

            direction,

            confidence,

            experience_level,

            strategy,

        )

        return {

            "repository_phase":
                phase,

            "technical_direction":
                direction,

            "knowledge_confidence":
                confidence,

            "experience_level":
                experience_level,

            "engineering_strategy":
                strategy,

            "executive_priority":
                priority,

            "risk":
                risk,

            "recommended_next_step":
                next_step,

            "executive_reasoning":
                reasoning,

            "summary":
                (
                    f"Repository strategy selected: "
                    f"{strategy}."
                ),

            "version":
                self.VERSION,

        }

    # --------------------------------------------------

    def _decide_strategy(

        self,

        phase,

        direction,

        experience,

        confidence,

    ):

        # Recovery always wins

        if phase == "Recovery":

            return "Aggressive Technical Debt Reduction"

        # Stable repository

        if phase == "Stabilization":

            if confidence >= 0.90:

                return "Continuous Quality Expansion"

            if confidence >= 0.70:

                return "Repository-wide Refactoring"

            return "Knowledge Consolidation"

        # Growing repository

        if phase == "Expansion":

            if experience in [

                "Senior",

                "Principal",

            ]:

                return "Controlled Feature Expansion"

            return "Engineering Capability Growth"

        # Direction fallback

        if direction == "Positive":

            return "Continuous Engineering Improvement"

        if direction == "Negative":

            return "Repository Recovery Plan"

        return "Monitor Repository Evolution"

    # --------------------------------------------------

    def _priority(

        self,

        strategy,

    ):

        if strategy in [

            "Aggressive Technical Debt Reduction",

            "Repository Recovery Plan",

        ]:

            return "CRITICAL"

        if strategy in [

            "Controlled Feature Expansion",

            "Continuous Quality Expansion",

            "Repository-wide Refactoring",

        ]:

            return "HIGH"

        return "NORMAL"

    # --------------------------------------------------

    def _risk(

        self,

        confidence,

        experience,

    ):

        if confidence >= 0.90 and experience in [

            "Senior",

            "Principal",

        ]:

            return "LOW"

        if confidence >= 0.70:

            return "MEDIUM"

        return "HIGH"

    # --------------------------------------------------

    def _next_step(

        self,

        strategy,

    ):

        mapping = {

            "Continuous Quality Expansion":
                "Expand repository engineering capabilities.",

            "Repository-wide Refactoring":
                "Improve repository architecture.",

            "Knowledge Consolidation":
                "Increase repository knowledge quality.",

            "Controlled Feature Expansion":
                "Develop new engineering capabilities.",

            "Engineering Capability Growth":
                "Improve engineering maturity.",

            "Aggressive Technical Debt Reduction":
                "Reduce repository complexity.",

            "Repository Recovery Plan":
                "Stabilize repository health.",

            "Continuous Engineering Improvement":
                "Continue engineering evolution.",

            "Monitor Repository Evolution":
                "Observe future repository changes.",

        }

        return mapping.get(

            strategy,

            "Continue engineering.",

        )

    # --------------------------------------------------

    def _reasoning(

        self,

        phase,

        direction,

        confidence,

        experience,

        strategy,

    ):

        return (

            f"The repository is currently in the "
            f"'{phase}' phase with a "
            f"'{direction}' engineering direction. "
            f"Knowledge confidence is "
            f"{confidence:.2f} while engineering "
            f"experience is '{experience}'. "
            f"Based on these signals Graphify "
            f"selected the strategy "
            f"'{strategy}'."

        )