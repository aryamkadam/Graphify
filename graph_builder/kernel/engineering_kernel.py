"""
Graphify

Stage 30.0

Engineering Kernel

The Engineering Kernel is the central
orchestrator of the AI Software Engineering
Operating System.

Responsibilities

• Receive engineering tasks
• Consult Decision Engine
• Orchestrate engineering workers
• Store engineering experience
• Return final engineering outcome

Author:
Graphify Core
"""

from graph_builder.decision.engineering_decision_engine import (
    EngineeringDecisionEngine,
)

from graph_builder.workers.repository_architect_worker import (
    RepositoryArchitectWorker,
)

from graph_builder.workers.code_engineer_worker import (
    CodeEngineerWorker,
)

from graph_builder.workers.testing_engineer_worker import (
    TestingEngineerWorker,
)

from graph_builder.workers.engineering_review_cycle import (
    EngineeringReviewCycle,
)


class EngineeringKernel:

    VERSION = "30.0"

    def __init__(self):

        self.decision_engine = EngineeringDecisionEngine()

        self.architect = RepositoryArchitectWorker()

        self.engineer = CodeEngineerWorker()

        self.tester = TestingEngineerWorker()

        self.review_cycle = EngineeringReviewCycle()

    # --------------------------------------------------

    def execute(

        self,

        task,

    ):

        decision = self.decision_engine.decide(

            task.to_dict()

        )

        architecture = self.architect.think()

        implementation = self.engineer.execute(

            task.title

        )

        validation = self.tester.validate(

            task.title

        )

        review = self.review_cycle.execute(task)

        self.decision_engine.remember(review)

        return {

            "status": "success",

            "task": task.to_dict(),

            "decision": decision,

            "architecture": architecture,

            "implementation": implementation,

            "validation": validation,

            "review": review,

            "version": self.VERSION,

        }

    # --------------------------------------------------

    def status(self):

        return {

            "kernel": "ONLINE",

            "version": self.VERSION,

            "workers": [

                self.architect.worker_name,

                self.engineer.worker_name,

                self.tester.worker_name,

            ],

        }