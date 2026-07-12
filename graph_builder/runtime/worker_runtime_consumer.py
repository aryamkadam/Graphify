"""
Graphify

Stage 47.0

Worker Runtime Consumer
"""


class WorkerRuntimeConsumer:

    VERSION = "47.0"

    def __init__(

        self,

        inbox_manager,

    ):

        self.inbox = inbox_manager

    # ----------------------------------------

    def consume(self, worker):

        message = self.inbox.receive(worker)

        if message is None:

            return {

                "worker": worker,

                "status": "IDLE",

                "version": self.VERSION,

            }

        return {

            "worker": worker,

            "status": "PROCESSING",

            "execution_id": message["execution_id"],

            "action": message["action"],

            "version": self.VERSION,

        }