"""
Stage 17.4

Repository Decision Graph Engine

Transforms engineering cause-effect chains
into reusable engineering decisions.

These decisions become permanent Repository Brain
knowledge and can later be transferred to any AI.
"""


class RepositoryDecisionGraphEngine:

    def build(self, cause_effect_report):

        chains = cause_effect_report.get("cause_effect_chains", [])

        decision_graph = []

        for chain in chains:

            decision = self._create_decision(chain)

            decision_graph.append(decision)

        return {

            "decision_graph": decision_graph,

            "summary": (
                f"{len(decision_graph)} engineering decisions captured "
                "for Repository Brain."
            )

        }

    # --------------------------------------------

    def _create_decision(self, chain):

        impact = self._calculate_impact(chain)

        confidence = self._calculate_confidence(chain)

        return {

            "decision": self._decision_name(chain),

            "causes": chain["causes"],

            "direct_effects": chain["direct_effects"],

            "future_effects": chain["future_effects"],

            "impact": impact,

            "confidence": confidence

        }

    # --------------------------------------------

    def _decision_name(self, chain):

        if "technical debt decreased" in chain["causes"]:

            return "Refactoring Improved Repository"

        if "repository health improved" in chain["causes"]:

            return "Quality Improvement Decision"

        if "execution capabilities expanded" in chain["causes"]:

            return "Repository Capability Expansion"

        return "Engineering Decision"

    # --------------------------------------------

    def _calculate_impact(self, chain):

        score = (

            len(chain["direct_effects"])

            + len(chain["future_effects"])

        )

        if score >= 6:

            return "High"

        if score >= 4:

            return "Medium"

        return "Low"

    # --------------------------------------------

    def _calculate_confidence(self, chain):

        score = len(chain["causes"])

        return min(1.0, round(0.55 + score * 0.10, 2))