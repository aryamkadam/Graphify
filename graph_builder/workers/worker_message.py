"""
Graphify

Phase 2

Stage P2.7

Worker Message

Represents communication between
engineering workers.

Author:
Graphify Core
"""


class WorkerMessage:

    VERSION = "P2.7"

    def __init__(

        self,

        sender,

        receiver,

        message_type,

        content,

    ):

        self.sender = sender
        self.receiver = receiver
        self.message_type = message_type
        self.content = content

    # --------------------------------------------------

    def to_dict(self):

        return {

            "from": self.sender,

            "to": self.receiver,

            "type": self.message_type,

            "content": self.content,

            "version": self.VERSION,

        }