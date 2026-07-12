"""
Graphify

Stage 48.0

Base Worker
"""


class BaseWorker:

    VERSION = "48.0"

    def __init__(

        self,

        name,

    ):

        self.name = name

        self.state = "IDLE"

    # -----------------------------

    def think(self):

        return {

            "worker": self.name,

            "decision": "Thinking...",

            "version": self.VERSION,

        }

    # -----------------------------

    def execute(

        self,

        task,

    ):

        self.state = "WORKING"

        return {

            "worker": self.name,

            "task": task,

            "status": "EXECUTED",

            "version": self.VERSION,

        }

    # -----------------------------

    def report(self):

        return {

            "worker": self.name,

            "state": self.state,

            "version": self.VERSION,

        }