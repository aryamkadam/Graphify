"""
Graphify

Stage 46.0

Worker Inbox Manager
"""

from collections import defaultdict, deque


class WorkerInboxManager:

    VERSION = "46.0"

    def __init__(self):

        self._inboxes = defaultdict(deque)

    # --------------------------------

    def deliver(self, message):

        worker = message["worker"]

        self._inboxes[worker].append(message)

    # --------------------------------

    def receive(self, worker):

        if not self._inboxes[worker]:
            return None

        return self._inboxes[worker].popleft()

    # --------------------------------

    def pending(self, worker):

        return len(self._inboxes[worker])

    # --------------------------------

    def status(self):

        return {

            worker: len(queue)

            for worker, queue in self._inboxes.items()

        }