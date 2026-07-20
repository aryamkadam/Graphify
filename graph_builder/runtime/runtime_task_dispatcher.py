"""
Graphify

Phase 10

Stage P10.5

Runtime Task Dispatcher

Transforms Engineering Tasks into
a Runtime Execution Queue.

Author:
Graphify Core
"""

from datetime import datetime


class RuntimeTaskDispatcher:

    VERSION = "P10.5"

    def dispatch(self, task_bundle):

        queue = []

        for order, task in enumerate(task_bundle["tasks"], start=1):

            queue.append({

                "queue_position": order,

                "task_id": task["task_id"],

                "worker": task["worker"],

                "priority": task["priority"],

                "status": "QUEUED",

                "depends_on": task["depends_on"],

                "queued_at": datetime.utcnow().isoformat() + "Z",

            })

        return {

            "repository_objective": task_bundle["repository_objective"],

            "queue_size": len(queue),

            "runtime_queue": queue,

            "version": self.VERSION,

        }