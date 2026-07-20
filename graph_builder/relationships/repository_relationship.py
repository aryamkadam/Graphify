"""
Graphify

Phase 11

Stage P11.5

Repository Relationship

Represents one engineering relationship.

Author:
Graphify Core
"""

from dataclasses import dataclass


@dataclass
class RepositoryRelationship:

    VERSION = "P11.5"

    source: str

    relationship: str

    target: str

    module: str

    line: int

    def to_dict(self):

        return {

            "source": self.source,

            "relationship": self.relationship,

            "target": self.target,

            "module": self.module,

            "line": self.line,

            "version": self.VERSION,

        }