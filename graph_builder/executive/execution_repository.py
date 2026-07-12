"""
Graphify

Stage 43.0

Execution Repository
"""


class ExecutionRepository:

    VERSION = "43.0"

    def __init__(self):

        self._executions = {}

    # ------------------------------

    def add(self, execution):

        self._executions[
            execution["execution_id"]
        ] = execution

    # ------------------------------

    def get(self, execution_id):

        return self._executions.get(
            execution_id
        )

    # ------------------------------

    def all(self):

        return list(
            self._executions.values()
        )

    # ------------------------------

    def by_worker(self, worker):

        return [

            execution

            for execution in self._executions.values()

            if execution["worker"] == worker

        ]

    # ------------------------------

    def by_status(self, status):

        return [

            execution

            for execution in self._executions.values()

            if execution["status"] == status

        ]

    # ------------------------------

    def status(self):

        return {

            "executions": len(self._executions),

            "version": self.VERSION,

        }