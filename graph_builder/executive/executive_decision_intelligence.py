"""
Graphify

Phase 5

Stage P5.10

Executive Decision Intelligence

Combines executive strategy, recall,
prediction and learning into a single
engineering decision.

Author:
Graphify Core
"""


class ExecutiveDecisionIntelligence:

    VERSION = "P5.10"

    # --------------------------------------------------

    def build(

        self,

        strategy,

        recall,

        prediction,

    ):

        engineering_strategy = strategy.get(

            "engineering_strategy",

            "Unknown",

        )

        confidence = prediction.get(

            "confidence",

            0.50,

        )

        predicted_outcome = prediction.get(

            "predicted_outcome",

            "Unknown",

        )

        recall_matches = recall.get(

            "matches",

            0,

        )

        if confidence >= 0.90:

            priority = "HIGH"

        elif confidence >= 0.70:

            priority = "MEDIUM"

        else:

            priority = "LOW"

        decision = self._decision(

            engineering_strategy,

            confidence,

        )

        return {

            "executive_decision": decision,

            "priority": priority,

            "confidence": confidence,

            "reasoning":

                f"{recall_matches} similar executive decisions were recalled. "

                f"Predicted outcome: {predicted_outcome}.",

            "recommended_next_action":

                engineering_strategy,

            "version":

                self.VERSION,

        }

    # --------------------------------------------------

    def _decision(

        self,

        strategy,

        confidence,

    ):

        if confidence >= 0.90:

            return (

                f"Proceed aggressively with '{strategy}'."

            )

        elif confidence >= 0.70:

            return (

                f"Proceed cautiously with '{strategy}'."

            )

        return (

            "Collect additional engineering evidence before major changes."

        )