"""
Stage 17.4

Repository Decision Graph Engine

Converts repository evolution into reusable
engineering decisions.

Future AI systems consume decisions rather
than raw repository metrics.

This becomes part of the Repository Brain.
"""


class RepositoryDecisionGraphEngine:

    def build(self, cause_effect_report):

        chains = cause_effect_report.get(

            "cause_effect_chains",

            []

        )

        decisions = []

        for chain in chains:

            decisions.append(

                self._decision(chain)

            )

        return {

            "decision_graph": decisions,

            "summary": self._summary(decisions)

        }

    # ---------------------------------------------

    def _decision(self, chain):

        causes = chain["causes"]

        decision = "Repository Evolution"

        confidence = 0.80

        impact = "Medium"

        if "technical debt decreased" in causes:

            decision = "Refactoring Improved Repository"

            confidence = 0.95

            impact = "High"

        elif "execution capabilities expanded" in causes:

            decision = "Repository Capability Expansion"

            confidence = 0.90

            impact = "High"

        elif "repository health improved" in causes:

            decision = "Engineering Quality Improvement"

            confidence = 0.90

            impact = "High"

        elif "hotspots became more stable" in causes:

            decision = "Architecture Stabilization"

            confidence = 0.88

            impact = "Medium"

        return {

            "decision": decision,

            "confidence": confidence,

            "impact": impact,

            "causes": chain["causes"],

            "direct_effects": chain["direct_effects"],

            "future_effects": chain["future_effects"]

        }

    # ---------------------------------------------

    def _summary(self, decisions):

        if not decisions:

            return "No engineering decisions detected."

        return (

            f"{len(decisions)} engineering decisions "

            f"captured for Repository Brain."

        )