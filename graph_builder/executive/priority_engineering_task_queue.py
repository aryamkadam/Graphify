"""
Graphify

Stage 59.2

Priority Engineering Task Queue

Stores engineering work ordered
by priority.

Author:
Graphify Core
"""

import heapq


class PriorityEngineeringTaskQueue:

    VERSION = "59.2"

    def __init__(self):

        self._queue = []

        self._counter = 0

    # --------------------------------------------------

    def push(

        self,

        task,

        priority=50,

    ):

        heapq.heappush(

            self._queue,

            (

                -priority,

                self._counter,

                task,

            ),

        )

        self._counter += 1

    # --------------------------------------------------

    def pop(self):

        if not self._queue:

            return None

        priority, _, task = heapq.heappop(

            self._queue

        )

        return {

            "task": task,

            "priority": -priority,

        }

    # --------------------------------------------------

    def peek(self):

        if not self._queue:

            return None

        priority, _, task = self._queue[0]

        return {

            "task": task,

            "priority": -priority,

        }

    # --------------------------------------------------

    def size(self):

        return len(self._queue)

    # --------------------------------------------------

    def empty(self):

        return len(self._queue) == 0

    # --------------------------------------------------

    def clear(self):

        self._queue.clear()

    # --------------------------------------------------

    def status(self):

        return {

            "tasks": self.size(),

            "empty": self.empty(),

            "version": self.VERSION,

        }