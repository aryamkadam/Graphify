"""
Graphify

Phase 15

Stage P15.1

Repository Understanding

Represents Graphify's semantic understanding
of an entire repository.

Author:
Graphify Core
"""

from dataclasses import dataclass, field


@dataclass
class RepositoryUnderstanding:

    VERSION = "P15.1"

    repository: str

    # Existing intelligence

    identity: str = ""

    mission: str = ""

    goals: list[str] = field(default_factory=list)

    # Repository meaning

    engineering_scope: str = ""

    current_focus: str = ""

    architecture_summary: str = ""

    # Future cognition

    strengths: list[str] = field(default_factory=list)

    weaknesses: list[str] = field(default_factory=list)

    technical_debt: list[str] = field(default_factory=list)

    architectural_risks: list[str] = field(default_factory=list)

    evolution_opportunities: list[str] = field(default_factory=list)

    confidence: float = 0.0

    # --------------------------------------------------

    def summary(self):

        return {

            "repository": self.repository,

            "identity": self.identity,

            "mission": self.mission,

            "goal_count": len(self.goals),

            "strengths": len(self.strengths),

            "weaknesses": len(self.weaknesses),

            "technical_debt": len(self.technical_debt),

            "architectural_risks": len(self.architectural_risks),

            "confidence": self.confidence,

            "version": self.VERSION,

        }