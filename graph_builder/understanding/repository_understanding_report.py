"""
Graphify

Phase 22

Stage P22.1

Repository Understanding Report

Represents the current architectural understanding
of the active repository.

This report is descriptive only.

It never performs reasoning.
It never performs planning.
It never performs engineering.

Author:
Graphify Core
"""

from dataclasses import dataclass, field
from datetime import datetime, UTC


@dataclass(frozen=True)
class RepositoryUnderstandingReport:

    VERSION = "P22.1"

    # --------------------------------------------------
    # Repository
    # --------------------------------------------------

    repository_name: str

    repository_path: str

    timestamp: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    # --------------------------------------------------
    # Architectural Understanding
    # --------------------------------------------------

    architecture_style: str = "UNKNOWN"

    module_organization: str = "UNKNOWN"

    dependency_summary: str = "UNKNOWN"

    structural_complexity: str = "UNKNOWN"

    # --------------------------------------------------
    # Repository Understanding
    # --------------------------------------------------

    architectural_strengths: list[str] = field(
        default_factory=list
    )

    architectural_weaknesses: list[str] = field(
        default_factory=list
    )

    confidence: float = 0.0

    # --------------------------------------------------

    def status(self):

        return {

            "repository":
                self.repository_name,

            "architecture_style":
                self.architecture_style,

            "module_organization":
                self.module_organization,

            "dependency_summary":
                self.dependency_summary,

            "structural_complexity":
                self.structural_complexity,

            "strengths":
                self.architectural_strengths,

            "weaknesses":
                self.architectural_weaknesses,

            "confidence":
                self.confidence,

            "timestamp":
                self.timestamp,

            "version":
                self.VERSION,

        }