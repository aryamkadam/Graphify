"""
Graphify

Phase 21

Stage P21.1

Repository Awareness Report

Represents the current awareness snapshot
of a loaded repository.

This object contains only observations.

It never performs reasoning,
planning,
or engineering.

Produced by:
    RepositoryAwarenessEngine

Consumed by:
    RepositoryAwarenessManager
    Decision Engine
    Planning Engine
    Executive Engine

Author:
Graphify Core
"""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass(frozen=True)
class RepositoryAwarenessReport:

    VERSION = "P21.1"

    # --------------------------------------------------
    # Repository
    # --------------------------------------------------

    repository_name: str

    repository_path: str

    timestamp: datetime

    # --------------------------------------------------
    # Awareness
    # --------------------------------------------------

    identity: str

    capability: str

    behavior: str

    # --------------------------------------------------
    # Runtime
    # --------------------------------------------------

    state: str

    health: str

    runtime_ready: bool

    # --------------------------------------------------
    # Cognitive Status
    # --------------------------------------------------

    memory_loaded: bool

    evolution_loaded: bool

    brain_loaded: bool

    # --------------------------------------------------
    # Diagnostics
    # --------------------------------------------------

    warnings: list[str] = field(default_factory=list)

    # --------------------------------------------------

    def status(self):

        return {

            "repository": self.repository_name,

            "identity": self.identity,

            "capability": self.capability,

            "behavior": self.behavior,

            "state": self.state,

            "health": self.health,

            "runtime_ready": self.runtime_ready,

            "memory_loaded": self.memory_loaded,

            "evolution_loaded": self.evolution_loaded,

            "brain_loaded": self.brain_loaded,

            "warnings": self.warnings,

            "timestamp": self.timestamp,

            "version": self.VERSION,

        }