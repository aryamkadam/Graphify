"""
Graphify

Stage 44.0

Runtime Execution Orchestrator
"""

class RuntimeExecutionOrchestrator:

    VERSION = "44.0"

    def __init__(

        self,

        repository,

        state_manager,

    ):

        self.repository = repository

        self.state_manager = state_manager

    # ----------------------------------

    def dispatch(self):

        dispatched = []

        for execution in self.repository.all():

            if execution["status"] != "QUEUED":

                continue

            self.state_manager.update(

                execution["execution_id"],

                "RUNNING",

            )

            dispatched.append(

                {

                    "execution_id": execution["execution_id"],

                    "worker": execution["worker"],

                    "node": execution["node"],

                    "status": "RUNNING",

                }

            )

        return dispatched