"""
Graphify

Phase 2

Stage P2.7

Collaboration Engine

Handles communication between workers.

Author:
Graphify Core
"""

from graph_builder.workers.worker_message import WorkerMessage


class CollaborationEngine:

    VERSION = "P2.7"

    def __init__(self):

        self.messages = []

    # --------------------------------------------------

    def send(

        self,

        sender,

        receiver,

        message_type,

        content,

    ):

        message = WorkerMessage(

            sender,

            receiver,

            message_type,

            content,

        )

        self.messages.append(message)

        return message.to_dict()

    # --------------------------------------------------

    def conversation(self):

        return [

            message.to_dict()

            for message in self.messages

        ]

    # --------------------------------------------------

    def status(self):

        return {

            "messages": len(self.messages),

            "version": self.VERSION,

        }