"""
Graphify

Phase 15

Stage P15.3

Repository Cognitive Reasoning

Author:
Graphify Core
"""


class RepositoryCognitiveReasoning:

    VERSION = "P15.3"

    def __init__(

        self,

        repository,

        engineering_conclusions,

        dominant_reasoning,

        repository_state,

        engineering_maturity,

        confidence,

    ):

        self.repository = repository

        self.engineering_conclusions = engineering_conclusions

        self.dominant_reasoning = dominant_reasoning

        self.repository_state = repository_state

        self.engineering_maturity = engineering_maturity

        self.confidence = confidence

    # ---------------------------------------------

    def summary(self):

        return {

            "repository": self.repository,

            "repository_state": self.repository_state,

            "dominant_reasoning": self.dominant_reasoning,

            "engineering_maturity": self.engineering_maturity,

            "conclusions": len(

                self.engineering_conclusions

            ),

            "confidence": self.confidence,

            "version": self.VERSION,

        }