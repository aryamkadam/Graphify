"""
Graphify

Phase 12

Stage P12.4

Repository Capability

Represents a high-level engineering capability
provided by a repository component.

Author:
Graphify Core
"""


class RepositoryCapability:

    VERSION = "P12.4"

    def __init__(
        self,
        module,
        capability,
        engineering_domain,
        confidence,
        evidence,
    ):

        self.module = module
        self.capability = capability
        self.engineering_domain = engineering_domain
        self.confidence = confidence
        self.evidence = evidence

    def to_dict(self):

        return {

            "module": self.module,
            "capability": self.capability,
            "engineering_domain": self.engineering_domain,
            "confidence": self.confidence,
            "evidence": self.evidence,
            "version": self.VERSION,

        }