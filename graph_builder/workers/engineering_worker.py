"""
Graphify

Phase 7

Stage P7.1

Engineering Worker

Foundation for every engineering
worker inside Graphify.

Every worker in Graphify inherits
from this class.

Author:
Graphify Core
"""


class EngineeringWorker:

    VERSION = "P7.1"

    def __init__(

        self,

        worker_name,

        role,

    ):

        self.worker_name = worker_name

        self.role = role

        self.status = "IDLE"

        self.current_task = None

    # --------------------------------------------------

    def assign(

        self,

        work_package,

    ):

        self.current_task = work_package

        self.status = "ASSIGNED"

    # --------------------------------------------------

    def start(self):

        if self.current_task is None:

            return

        self.status = "WORKING"

    # --------------------------------------------------

    def complete(

        self,

        result=None,

    ):

        report = {

            "worker": self.worker_name,

            "role": self.role,

            "task": self.current_task,

            "result": result,

            "status": "COMPLETED",

        }

        self.status = "IDLE"

        self.current_task = None

        return report

    # --------------------------------------------------

    def state(self):

        return {

            "worker": self.worker_name,

            "role": self.role,

            "status": self.status,

            "current_task": self.current_task,

            "version": self.VERSION,

        }