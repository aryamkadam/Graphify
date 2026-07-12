"""
Graphify

Stage 37.1

Graph Node

Base node for the Repository Engineering Graph.

Author:
Graphify Core
"""

from dataclasses import dataclass, field
from datetime import datetime
import uuid


@dataclass(slots=True)
class GraphNode:

    node_type: str

    name: str

    metadata: dict = field(default_factory=dict)

    node_id: str = field(default_factory=lambda: str(uuid.uuid4()))

    created_at: str = field(
        default_factory=lambda: datetime.utcnow().isoformat() + "Z"
    )

    VERSION = "37.1"

    def update_metadata(self, key, value):

        self.metadata[key] = value

    def to_dict(self):

        return {

            "node_id": self.node_id,

            "node_type": self.node_type,

            "name": self.name,

            "metadata": self.metadata,

            "created_at": self.created_at,

            "version": self.VERSION,

        }