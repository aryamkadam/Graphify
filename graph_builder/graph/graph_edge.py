"""
Graphify

Stage 37.2

Graph Edge

Represents a typed relationship
between two Graph Nodes.

Author:
Graphify Core
"""

from dataclasses import dataclass, field
from datetime import datetime
import uuid


@dataclass(slots=True)
class GraphEdge:

    source_id: str

    target_id: str

    relationship: str

    metadata: dict = field(default_factory=dict)

    edge_id: str = field(default_factory=lambda: str(uuid.uuid4()))

    created_at: str = field(
        default_factory=lambda: datetime.utcnow().isoformat() + "Z"
    )

    VERSION = "37.2"

    # --------------------------------------------------

    def update_metadata(self, key, value):

        self.metadata[key] = value

    # --------------------------------------------------

    def to_dict(self):

        return {

            "edge_id": self.edge_id,

            "source_id": self.source_id,

            "target_id": self.target_id,

            "relationship": self.relationship,

            "metadata": self.metadata,

            "created_at": self.created_at,

            "version": self.VERSION,

        }