"""
Graphify

Phase 11

Stage P11.6.1

Architecture Component

Represents one structural component
inside the repository.

Author:
Graphify Core
"""

from dataclasses import dataclass, field
from typing import List


@dataclass
class ArchitectureComponent:

    # Identity

    name: str

    path: str

    module: str

    # Architecture

    layer: str

    role: str

    visibility: str

    # Metrics

    symbol_count: int

    relationship_count: int

    importance: str

    # Future graph

    dependencies: List[str] = field(default_factory=list)

    dependents: List[str] = field(default_factory=list)

    architectural_neighbors: List[str] = field(default_factory=list)

    version: str = "P11.6.1"