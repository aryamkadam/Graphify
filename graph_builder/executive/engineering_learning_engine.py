"""
Graphify

Phase 5

Stage P5.2

Engineering Learning Engine

Transforms completed engineering execution
into learning decisions for workers.

Author:
Graphify Core
"""


class EngineeringLearningEngine:

    VERSION = "P5.2"

    def __init__(

        self,

        execution_report,

    ):

        self.execution = execution_report

    # --------------------------------------------------

    def build(self):

        learning = []

        report = self.execution.get(

            "report",

            [],

        )

        for item in report:

            learning.append(

                {

                    "worker":

                        item["worker"],

                    "task":

                        item["task"],

                    "experience_gain":

                        10,

                    "knowledge_gain":

                        5,

                    "confidence_gain":

                        2,

                }

            )

        return {

            "learning": learning,

            "summary":

                self._summary(

                    len(learning)

                ),

            "version":

                self.VERSION,

        }

    # --------------------------------------------------

    def _summary(

        self,

        completed,

    ):

        if completed == 0:

            return (

                "No engineering learning generated."

            )

        return (

            f"{completed} engineering learning "

            f"events generated."

        )