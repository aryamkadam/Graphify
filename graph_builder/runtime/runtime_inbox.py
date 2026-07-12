"""
Graphify

Stage 23.3

Runtime Inbox

Universal inbox for every Runtime Service.

Stores RuntimeMessages until the service
processes them.

Author:
Graphify Core
"""

from collections import deque


class RuntimeInbox:

    VERSION = "23.3"

    def __init__(self):

        self._messages = deque()

    # ------------------------------------------

    def push(

        self,

        message,

    ):

        self._messages.append(message)

    # ------------------------------------------

    def pop(self):

        if not self._messages:

            return None

        return self._messages.popleft()

    # ------------------------------------------

    def peek(self):

        if not self._messages:

            return None

        return self._messages[0]

    # ------------------------------------------

    def size(self):

        return len(self._messages)

    # ------------------------------------------

    def empty(self):

        return len(self._messages) == 0

    # ------------------------------------------

    def clear(self):

        self._messages.clear()

    # ------------------------------------------

    def status(self):

        return {

            "messages": self.size(),

            "empty": self.empty(),

            "version": self.VERSION,

        }