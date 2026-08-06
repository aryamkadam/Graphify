"""
Graphify

Phase 22

Stage P22.5

Repository Understanding

Canonical semantic understanding of an active repository.

Built directly from Repository Intelligence.

This object represents WHAT the repository is.

It never evaluates.

It never judges.

Author:
Graphify Core
"""

from dataclasses import dataclass


@dataclass
class RepositoryUnderstanding:

    VERSION = "P22.5"

    # --------------------------------------------------
    # Repository
    # --------------------------------------------------

    repository: str

    # --------------------------------------------------
    # Intelligence
    # --------------------------------------------------

    identity: object = None

    capability: object = None

    behavior: object = None

    # --------------------------------------------------
    # Understanding
    # --------------------------------------------------

    engineering_scope: str = ""

    architecture_description: str = ""

    repository_focus: str = ""

    organization_description: str = ""

    runtime_description: str = ""

    dependency_description: str = ""

    # --------------------------------------------------

    confidence: float = 0.0

    # --------------------------------------------------

    def summary(self):

        return {

            "repository": self.repository,

            "identity": self.identity,

            "capability": self.capability,

            "behavior": self.behavior,

            "engineering_scope": self.engineering_scope,

            "architecture_description": self.architecture_description,

            "repository_focus": self.repository_focus,

            "organization_description": self.organization_description,

            "runtime_description": self.runtime_description,

            "dependency_description": self.dependency_description,

            "confidence": self.confidence,

            "version": self.VERSION,

        }