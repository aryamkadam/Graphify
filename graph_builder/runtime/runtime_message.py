"""
Graphify

Stage 23.1

Runtime Message

Universal Runtime communication object.

Every Runtime Service communicates using
RuntimeMessage.

This becomes the official communication
protocol inside Graphify Runtime.

Author:
Graphify Core
"""

from datetime import datetime
import uuid


class RuntimeMessage:

    VERSION = "23.1"

    def __init__(

        self,

        source,

        target,

        event,

        payload=None,

    ):

        self.message_id = str(uuid.uuid4())

        self.source = source

        self.target = target

        self.event = event

        self.payload = payload or {}

        self.timestamp = datetime.utcnow().isoformat() + "Z"

    # --------------------------------------------------

    def to_dict(self):

        return {

            "message_id": self.message_id,

            "source": self.source,

            "target": self.target,

            "event": self.event,

            "payload": self.payload,

            "timestamp": self.timestamp,

            "version": self.VERSION,

        }

    # --------------------------------------------------

    def summary(self):

        return (

            f"[{self.event}] "

            f"{self.source} → {self.target}"

        )