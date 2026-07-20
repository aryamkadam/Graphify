"""
Graphify

Phase 5.0

Autonomous Engineering Loop

Coordinates one complete autonomous
engineering cycle.

Author:
Graphify Core
"""

from graph_builder.executive.autonomous_cto import AutonomousCTO
from graph_builder.executive.engineering_execution_engine import (
    EngineeringExecutionEngine,
)
from graph_builder.executive.executive_feedback_engine import (
    ExecutiveFeedbackEngine,
)


class AutonomousEngineeringLoop:

    VERSION = "P5.0"

    def __init__(

        self,

        repository_reasoning,

        registry,

    ):

        self.reasoning = repository_reasoning

        self.registry = registry

    # ------------------------------------------

    def run(self):

        cto = AutonomousCTO(

            self.reasoning

        )

        decision = cto.think()

        if not decision["approved"]:

            return {

                "status": "SPRINT_REJECTED",

                "decision": decision,

                "version": self.VERSION,

            }

        executor = EngineeringExecutionEngine(

            self.registry

        )

        execution = executor.execute(

            decision["engineering_sprint"]

        )

        feedback = ExecutiveFeedbackEngine(

            self.registry

        ).build()

        return {

            "status": "SPRINT_COMPLETED",

            "decision": decision,

            "execution": execution,

            "feedback": feedback,

            "version": self.VERSION,

        }