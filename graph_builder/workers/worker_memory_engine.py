"""
Graphify

Phase 7

Stage P7.7

Worker Memory Engine

Persistent engineering memory
for every worker.

Author:
Graphify Core
"""


class WorkerMemoryEngine:

    VERSION = "P7.7"

    def __init__(

        self,

        worker_name,

    ):

        self.worker_name = worker_name

        self._history = []

    # --------------------------------------------------

    def remember(

        self,

        engineering_task,

    ):

        self._history.append(

            {

                "title": engineering_task.title,

                "priority": engineering_task.priority,

                "result": engineering_task.actual_output,

            }

        )

    # --------------------------------------------------

    def history(self):

        return list(

            self._history,

        )

    # --------------------------------------------------

    def latest(self):

        if not self._history:

            return None

        return self._history[-1]

    # --------------------------------------------------

    def summary(self):

        latest = self.latest()

        return {

            "worker": self.worker_name,

            "completed_tasks": len(self._history),

            "latest_task": (

                latest["title"]

                if latest

                else None

            ),

            "version": self.VERSION,

        }