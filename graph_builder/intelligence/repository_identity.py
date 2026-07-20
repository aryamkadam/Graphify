"""
Graphify

Phase 12

Stage P12.5

Repository Identity

Represents the permanent engineering identity
of a software repository.

Author:
Graphify Core
"""


class RepositoryIdentity:

    VERSION = "P12.5"

    def __init__(
        self,
        repository,
        identity,
        engineering_type,
        confidence,
        capabilities,
    ):

        self.repository = repository
        self.identity = identity
        self.engineering_type = engineering_type
        self.confidence = confidence
        self.capabilities = capabilities

    def to_dict(self):

        return {

            "repository": self.repository,
            "identity": self.identity,
            "engineering_type": self.engineering_type,
            "confidence": self.confidence,
            "capabilities": self.capabilities,
            "version": self.VERSION,

        }