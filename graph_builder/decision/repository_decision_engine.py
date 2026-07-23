"""
Graphify

Phase 16

Stage P16.0

Repository Decision Engine

Author:
Graphify Core
"""

from graph_builder.decision.repository_decision import (
    RepositoryDecision,
)


class RepositoryDecisionEngine:

    VERSION = "P16.0"

    # -----------------------------------------

    def build(

        self,

        reasoning,

    ):

        goal = self._goal(reasoning)

        decision = self._decision(goal)

        reason = self._reason(reasoning, goal)

        priority = self._priority(reasoning)

        return RepositoryDecision(

            repository=reasoning.repository,

            selected_goal=goal,

            decision=decision,

            decision_reason=reason,

            priority=priority,

            confidence=reasoning.confidence,

        )

    # -----------------------------------------

    def _goal(

        self,

        reasoning,

    ):

        for conclusion in reasoning.engineering_conclusions:

            if "Technical debt" in conclusion:

                return "Reduce Technical Debt"

        return "Repository Evolution"

    # -----------------------------------------

    def _decision(

        self,

        goal,

    ):

        mapping = {

            "Reduce Technical Debt":
                "Prioritize Repository Refactoring",

            "Repository Evolution":
                "Continue Autonomous Evolution",

        }

        return mapping.get(

            goal,

            "Continue Engineering",

        )

    # -----------------------------------------

    def _reason(

        self,

        reasoning,

        goal,

    ):

        return (

            f"{goal} was selected because "

            f"{reasoning.dominant_reasoning.lower()} "

            f"is currently the dominant engineering reasoning."

        )

    # -----------------------------------------

    def _priority(

        self,

        reasoning,

    ):

        if reasoning.engineering_maturity == "HIGH":

            return "HIGH"

        return "MEDIUM"

    # -----------------------------------------

    def status(self):

        return {

            "engine":

            "Repository Decision Engine",

            "version": self.VERSION,

        }