"""
Graphify

Stage 21.1

Runtime Service

Base class for every Runtime Service.

Every Graphify Runtime component
inherits from this class.

Author:
Graphify Core
"""


class RuntimeService:

    VERSION = "21.1"

    def __init__(

        self,

        service_name,

    ):

        self.service_name = service_name

        self.state = "STOPPED"

        self.started = False

    # ------------------------------------------

    def start(self):

        self.state = "RUNNING"

        self.started = True

        return {

            "service": self.service_name,

            "state": self.state,

            "status": "success",

        }

    # ------------------------------------------

    def stop(self):

        self.state = "STOPPED"

        self.started = False

        return {

            "service": self.service_name,

            "state": self.state,

            "status": "success",

        }

    # ------------------------------------------

    def restart(self):

        self.stop()

        self.start()

        return {

            "service": self.service_name,

            "state": self.state,

            "status": "success",

        }

    # ------------------------------------------

    def status(self):

        return {

            "service": self.service_name,

            "running": self.started,

            "state": self.state,

            "version": self.VERSION,

        }
    