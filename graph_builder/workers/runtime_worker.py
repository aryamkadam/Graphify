"""
Graphify

Stage 24.1

Runtime Worker

Base class for every AI Worker inside
Graphify.

Workers are autonomous engineering
agents.

Author:
Graphify Core
"""

from graph_builder.runtime.runtime_inbox import RuntimeInbox


class RuntimeWorker:

    VERSION = "24.1"

    def __init__(

        self,

        worker_name,

    ):

        # Canonical worker identity
        self.worker_name = worker_name

        # Universal alias for future workers
        # Allows every worker to use self.name
        self.name = worker_name

        self.inbox = RuntimeInbox()

        self.state = "IDLE"

    # --------------------------------------------------

    def receive(

        self,

        message,

    ):

        self.inbox.push(message)

    # --------------------------------------------------

    def think(self):

        """
        Override in subclasses.
        """

        return None

    # --------------------------------------------------

    def execute(self):

        """
        Override in subclasses.
        """

        return None

    # --------------------------------------------------

    def status(self):

        return {

            "worker": self.worker_name,

            "state": self.state,

            "pending_messages": self.inbox.size(),

            "version": self.VERSION,

        }