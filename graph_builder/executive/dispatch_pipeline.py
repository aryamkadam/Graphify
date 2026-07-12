"""
Graphify

Stage 59.4

Dispatch Pipeline

Connects the Executive Scheduler with
the Worker Selection Engine and executes
tasks automatically.

Author:
Graphify Core
"""

from graph_builder.executive.executive_scheduler import (
    ExecutiveScheduler,
)

from graph_builder.executive.worker_selection_engine import (
    WorkerSelectionEngine,
)


class DispatchPipeline:

    VERSION = "59.4"

    def __init__(

        self,

        scheduler: ExecutiveScheduler,

        selector: WorkerSelectionEngine,

    ):

        self.scheduler = scheduler

        self.selector = selector

    # --------------------------------------------------

    def execute(

        self,

        task,

        task_type,

    ):

        queued = self.scheduler.submit(task)

        dispatched = self.scheduler.dispatch()

        if dispatched["status"] != "DISPATCHED":

            return {

                "status": "FAILED",

                "reason": "Scheduler idle",

                "version": self.VERSION,

            }

        worker = self.selector.select(task_type)

        if worker["status"] != "SELECTED":

            return {

                "status": "FAILED",

                "reason": "No suitable worker",

                "version": self.VERSION,

            }

        return {

            "status": "PIPELINE_COMPLETED",

            "task": task,

            "task_type": task_type,

            "worker": worker["worker"],

            "version": self.VERSION,

        }

    # --------------------------------------------------

    def status(self):

        return {

            "version": self.VERSION,

            "scheduler": self.scheduler.status(),

            "supported_roles": self.selector.supported_roles(),

        }