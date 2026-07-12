"""
Graphify

Stage 42.0

Execution State Manager

Author:
Graphify Core
"""


class ExecutionStateManager:

    VERSION = "42.0"

    VALID_STATES = {

        "QUEUED",

        "RUNNING",

        "COMPLETED",

        "FAILED",

        "RETRYING",

        "CANCELLED",

    }

    def __init__(self):

        self.executions = {}

    # -----------------------------------------

    def register(self, execution):

        self.executions[

            execution["execution_id"]

        ] = execution

    # -----------------------------------------

    def update(

        self,

        execution_id,

        state,

    ):

        if state not in self.VALID_STATES:

            raise ValueError(

                f"Invalid state: {state}"

            )

        self.executions[

            execution_id

        ]["status"] = state

    # -----------------------------------------

    def get(

        self,

        execution_id,

    ):

        return self.executions.get(

            execution_id

        )

    # -----------------------------------------

    def summary(self):

        counts = {}

        for execution in self.executions.values():

            state = execution["status"]

            counts[state] = counts.get(state, 0) + 1

        return {

            "states": counts,

            "total": len(self.executions),

            "version": self.VERSION,

        }