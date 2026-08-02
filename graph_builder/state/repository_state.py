"""
Graphify

Phase 20

Stage P20.1

Repository State

Represents the current state of a repository.

This object is the canonical state representation
used by reasoning, planning, engineering and future
autonomous systems.

Contains no business logic.

Author:
Graphify Core
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class RepositoryState:

    VERSION = "P20.1"

    #
    # Repository
    #

    repository: str

    repository_path: str

    #
    # Intelligence
    #

    identity: object

    capability: object

    behavior: object

    #
    # State Metrics
    #

    health_score: float = 0.0

    maturity_score: float = 0.0

    stability_score: float = 0.0

    confidence: float = 0.0

    #
    # Metadata
    #

    timestamp: datetime = field(default_factory=datetime.utcnow)

    metadata: dict = field(default_factory=dict)

    # -----------------------------------------------------

    def to_dict(self):

        return {

            "repository": self.repository,

            "repository_path": self.repository_path,

            "identity": self.identity,

            "capability": self.capability,

            "behavior": self.behavior,

            "health_score": self.health_score,

            "maturity_score": self.maturity_score,

            "stability_score": self.stability_score,

            "confidence": self.confidence,

            "timestamp": self.timestamp,

            "metadata": self.metadata,

            "version": self.VERSION,

        }

    # -----------------------------------------------------

    @property
    def ready(self):

        return (

            self.identity is not None

            and self.capability is not None

            and self.behavior is not None

        )