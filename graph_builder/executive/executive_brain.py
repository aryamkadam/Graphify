"""
Graphify

Phase 5

Stage P5.12

Executive Brain

Single executive entry point for Graphify.

The Executive Brain owns executive memory
and delegates reasoning to the Executive
Cognitive Core.

Author:
Graphify Core
"""

from graph_builder.executive.executive_memory_engine import (
    ExecutiveMemoryEngine,
)

from graph_builder.executive.executive_cognitive_core import (
    ExecutiveCognitiveCore,
)


class ExecutiveBrain:

    VERSION = "P5.12"

    def __init__(self):

        self.memory = ExecutiveMemoryEngine()

        self.core = ExecutiveCognitiveCore(

            self.memory,

        )

    # --------------------------------------------------

    def think(

        self,

        consciousness,

        knowledge,

        experience,

    ):

        executive_state = self.core.execute(

            consciousness,

            knowledge,

            experience,

        )

        return {

            "executive_state": "THINKING",

            "executive_decision":

                executive_state["decision"],

            "executive_strategy":

                executive_state["strategy"],

            "version":

                self.VERSION,

        }

    # --------------------------------------------------

    def executive_memory(self):

        return self.memory.export()

    # --------------------------------------------------

    def summary(self):

        return {

            "executive_decisions":

                self.memory.summary()["executive_decisions"],

            "version":

                self.VERSION,

        }