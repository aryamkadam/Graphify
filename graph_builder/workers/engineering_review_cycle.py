"""
Graphify

Stage 27.0

Engineering Review Cycle

Coordinates iterative engineering until
quality checks pass.

Author:
Graphify Core
"""

from graph_builder.workers.repository_architect_worker import RepositoryArchitectWorker
from graph_builder.workers.code_engineer_worker import CodeEngineerWorker
from graph_builder.workers.testing_engineer_worker import TestingEngineerWorker


class EngineeringReviewCycle:

    VERSION = "27.0"

    def __init__(self):

        self.architect = RepositoryArchitectWorker()

        self.engineer = CodeEngineerWorker()

        self.tester = TestingEngineerWorker()

    # --------------------------------------------------

    def execute(

        self,

        task,

    ):

        history = []

        architect_result = self.architect.think()

        history.append(

            {

                "worker": self.architect.worker_name,

                "decision": architect_result,

            }

        )

        engineer_result = self.engineer.execute(

            task.title,

        )

        history.append(

            {

                "worker": self.engineer.worker_name,

                "implementation": engineer_result,

            }

        )

        testing_result = self.tester.validate(

            task,

        )

        history.append(

            {

                "worker": self.tester.worker_name,

                "validation": testing_result,

            }

        )

        if testing_result["result"] == "VERIFIED":

            task.complete()

            final_status = "COMPLETED"

        else:

            final_status = "REQUIRES_REVISION"

        return {

            "status": "success",

            "task": task.to_dict(),

            "final_status": final_status,

            "history": history,

            "version": self.VERSION,

        }