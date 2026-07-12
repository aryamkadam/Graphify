"""
Graphify

Stage 59.1

Executive Scheduler

Responsible for dispatching engineering
tasks from the queue.

Author:
Graphify Core
"""

from graph_builder.executive.engineering_task_queue import (
    EngineeringTaskQueue,
)


class ExecutiveScheduler:

    VERSION = "59.1"

    def __init__(self):

        self.queue = EngineeringTaskQueue()

    # --------------------------------------------------

    def submit(self, task):

        self.queue.push(task)

        return {

            "task": task,

            "status": "QUEUED",

            "version": self.VERSION,

        }

    # --------------------------------------------------

    def dispatch(self):

        task = self.queue.pop()

        if task is None:

            return {

                "status": "IDLE",

                "version": self.VERSION,

            }

        return {

            "task": task,

            "status": "DISPATCHED",

            "version": self.VERSION,

        }

    # --------------------------------------------------

    def status(self):

        return {

            "queue": self.queue.status(),

            "version": self.VERSION,

        }