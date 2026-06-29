"""
Stage 17.3

Repository Cause & Effect Engine

Converts repository evolution into engineering
cause → effect chains.

Future AI agents can understand WHY repository
knowledge changed and WHAT engineering impact
was produced.
"""


class RepositoryCauseEffectEngine:

    def build(

        self,

        explanation_report,

        learning_report,

    ):

        explanations = explanation_report.get(

            "explanations",

            []

        )

        patterns = learning_report.get(

            "patterns",

            {}

        )

        chains = []

        for explanation in explanations:

            chains.append(

                self._build_chain(

                    explanation,

                    patterns,

                )

            )

        return {

            "cause_effect_chains": chains,

            "summary": self._summary(chains)

        }

    # ------------------------------------------------

    def _build_chain(

        self,

        explanation,

        patterns,

    ):

        causes = explanation["because"]

        direct = []

        indirect = []

        future = []

        # ----------------------------

        if "repository health improved" in causes:

            direct.append(

                "Repository quality increased"

            )

        if "technical debt decreased" in causes:

            direct.append(

                "Maintenance became easier"

            )

        if "execution capabilities expanded" in causes:

            direct.append(

                "Repository functionality increased"

            )

        if "hotspots became more stable" in causes:

            direct.append(

                "Architecture became more predictable"

            )

        # ----------------------------

        if patterns.get(

            "health_trend"

        ) == "improving":

            indirect.append(

                "Engineering confidence increased"

            )

        if patterns.get(

            "technical_debt"

        ) == "decreasing":

            indirect.append(

                "Future refactoring effort reduced"

            )

        if patterns.get(

            "execution_growth"

        ) == "expanding":

            indirect.append(

                "Repository complexity continues to grow"

            )

        # ----------------------------

        future.append(

            "Repository Brain becomes more accurate"

        )

        future.append(

            "Future AI agents require less manual explanation"

        )

        future.append(

            "Repository knowledge becomes easier to transfer"

        )

        return {

            "change": explanation["change"],

            "from": explanation["from"],

            "to": explanation["to"],

            "causes": causes,

            "direct_effects": direct,

            "indirect_effects": indirect,

            "future_effects": future

        }

    # ------------------------------------------------

    def _summary(

        self,

        chains,

    ):

        if not chains:

            return (

                "No engineering cause-effect chains detected."

            )

        return (

            f"{len(chains)} engineering cause-effect chains generated."

        )