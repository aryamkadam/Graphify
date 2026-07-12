"""
Graphify

Stage 59.0

Engineering Task Queue

Central queue for all engineering work.

Author:
Graphify Core
"""

from collections import deque


class EngineeringTaskQueue:

    VERSION = "59.0"

    def __init__(self):

        self._queue = deque()

    # --------------------------------------------------

    def push(self, task):

        self._queue.append(task)

        return task

    # --------------------------------------------------

    def pop(self):

        if not self._queue:

            return None

        return self._queue.popleft()

    # --------------------------------------------------

    def peek(self):

        if not self._queue:

            return None

        return self._queue[0]

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