"""
Graphify

Phase 8

Stage P8.4

Repository Event

Represents one observable repository
event that may trigger an engineering
cycle.

Author:
Graphify Core
"""

import uuid
from datetime import datetime


class RepositoryEvent:

    VERSION = "P8.4"

    def __init__(

        self,

        event_type,

        reason,

        requires_engineering=False,

    ):

        self.event_id = str(uuid.uuid4())

        self.event_type = event_type

        self.reason = reason

        self.requires_engineering = requires_engineering

        self.created_at = datetime.utcnow().isoformat() + "Z"

    # --------------------------------------------------

    def to_dict(self):

        return {

            "event_id": self.event_id,

            "event_type": self.event_type,

            "reason": self.reason,

            "requires_engineering": self.requires_engineering,

            "created_at": self.created_at,

            "version": self.VERSION,

        }