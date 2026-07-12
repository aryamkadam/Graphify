"""
Graphify

Stage 45.0

Runtime Message Bus
"""

from collections import deque


class RuntimeMessageBus:

    VERSION = "45.0"

    def __init__(self):

        self._queue = deque()

    # ----------------------------

    def publish(self, message):

        self._queue.append(message)

    # ----------------------------

    def consume(self):

        if not self._queue:
            return None

        return self._queue.popleft()

    # ----------------------------

    def pending(self):

        return len(self._queue)

    # ----------------------------

    def empty(self):

        return len(self._queue) == 0

    # ----------------------------

    def status(self):

        return {

            "pending_messages": self.pending(),

            "version": self.VERSION,

        }