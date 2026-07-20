"""
Graphify

Phase 10

Stage P10.6

Runtime Worker Scheduler

Selects the next executable task
from the Runtime Queue.

Author:
Graphify Core
"""


class RuntimeWorkerScheduler:

    VERSION = "P10.6"

    def schedule(self, runtime_queue):

        queue = runtime_queue["runtime_queue"]

        completed = set()

        ready = []

        for task in queue:

            dependency = task["depends_on"]

            if dependency is None:

                task["status"] = "READY"

                ready.append(task)

            elif dependency in completed:

                task["status"] = "READY"

                ready.append(task)

        return {

            "repository_objective":
                runtime_queue["repository_objective"],

            "ready_tasks": ready,

            "ready_count": len(ready),

            "version": self.VERSION,

        }