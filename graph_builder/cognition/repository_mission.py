"""
Graphify

Phase 13

Stage P13.1

Repository Mission

Represents the engineering mission
of a repository.

A mission explains WHY the repository exists.

Author:
Graphify Core
"""

from dataclasses import dataclass


@dataclass(slots=True)
class RepositoryMission:

    VERSION = "P13.1"

    repository: str

    identity: str

    mission: str

    engineering_scope: str

    confidence: float

    # ------------------------------------------

    def summary(self):

        return {

            "repository": self.repository,

            "identity": self.identity,

            "mission": self.mission,

            "engineering_scope": self.engineering_scope,

            "confidence": self.confidence,

            "version": self.VERSION,

        }

    # ------------------------------------------

    def to_dict(self):

        return {

            "repository": self.repository,

            "identity": self.identity,

            "mission": self.mission,

            "engineering_scope": self.engineering_scope,

            "confidence": self.confidence,

            "version": self.VERSION,

        }