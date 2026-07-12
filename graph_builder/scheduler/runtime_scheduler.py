"""
Graphify

Stage 31.0

Runtime Scheduler

Schedules engineering workers
inside the Engineering Kernel.

Author:
Graphify Core
"""


class RuntimeScheduler:

    VERSION = "31.0"

    def __init__(self):

        self._queue = []

    # --------------------------------------------------

    def schedule(

        self,

        worker_name,

        action,

    ):

        self._queue.append(

            {

                "worker": worker_name,

                "action": action,

            }

        )

        return {

            "status": "success",

            "queued": len(self._queue),

            "version": self.VERSION,

        }

    # --------------------------------------------------

    def next(self):

        if not self._queue:

            return None

        return self._queue.pop(0)

    # --------------------------------------------------

    def pending(self):

        return len(self._queue)

    # --------------------------------------------------

    def empty(self):

        return self.pending() == 0

    # --------------------------------------------------

    def status(self):

        return {

            "version": self.VERSION,

            "pending": self.pending(),

            "empty": self.empty(),

        }