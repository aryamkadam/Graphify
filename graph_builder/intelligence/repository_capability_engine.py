"""
Graphify

Phase 12

Stage P12.4

Repository Capability Engine

Transforms engineering behaviors into
repository capabilities.

Author:
Graphify Core
"""

from graph_builder.intelligence.repository_capability import (
    RepositoryCapability,
)


class RepositoryCapabilityEngine:

    VERSION = "P12.4"

    def build(

        self,

        behavior_report,

    ):

        capability = self._capability(

            behavior_report["primary_behavior"]

        )

        domain = self._domain(

            capability

        )

        return RepositoryCapability(

            module=behavior_report["module"],

            capability=capability,

            engineering_domain=domain,

            confidence=behavior_report["behavior_confidence"],

            evidence=behavior_report["behavior_keywords"],

        )

    # ------------------------------------------------

    def _capability(

        self,

        behavior,

    ):

        mapping = {

            "Repository Learning":
                "Engineering Knowledge Acquisition",

            "Knowledge Recording":
                "Repository Knowledge Management",

            "Feedback Processing":
                "Engineering Feedback Intelligence",

            "Runtime Execution":
                "Execution Orchestration",

            "Engineering Planning":
                "Engineering Planning",

            "Engineering Reasoning":
                "Engineering Decision Making",

            "Repository Memory":
                "Persistent Engineering Memory",

            "Knowledge Graph":
                "Repository Graph Intelligence",

            "Repository Parsing":
                "Repository Structural Understanding",

            "Repository Scanning":
                "Repository Discovery",

        }

        return mapping.get(

            behavior,

            "General Repository Intelligence",

        )

    # ------------------------------------------------

    def _domain(

        self,

        capability,

    ):

        if "Knowledge" in capability:

            return "Knowledge"

        if "Memory" in capability:

            return "Memory"

        if "Decision" in capability:

            return "Reasoning"

        if "Planning" in capability:

            return "Planning"

        if "Execution" in capability:

            return "Runtime"

        if "Graph" in capability:

            return "Knowledge Graph"

        return "Infrastructure"