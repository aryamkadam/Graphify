"""
Graphify

Phase 12

Stage P12.5.1

Repository Identity Engine

Builds the engineering identity
of a repository.

Consumes:
    RepositoryCapability

Produces:
    RepositoryIdentity

Author:
Graphify Core
"""

from graph_builder.intelligence.repository_identity import (
    RepositoryIdentity,
)
from graph_builder.intelligence.repository_capability import (
    RepositoryCapability,
)


class RepositoryIdentityEngine:

    VERSION = "P12.5.1"

    # -------------------------------------------------

    def build(

        self,

        repository: str,

        capabilities: list[RepositoryCapability],

    ):

        capability_names = [

            capability.capability

            for capability in capabilities

        ]

        identity = self._infer_identity(

            capability_names,

        )

        engineering_type = self._engineering_type(

            identity,

        )

        confidence = self._confidence(

            capability_names,

        )

        return RepositoryIdentity(

            repository=repository,

            identity=identity,

            engineering_type=engineering_type,

            confidence=confidence,

            capabilities=capability_names,

        )

    # -------------------------------------------------

    def _infer_identity(

        self,

        capabilities: list[str],

    ) -> str:

        text = " ".join(capabilities)

        if (

            "Knowledge" in text

            and "Memory" in text

            and "Decision" in text

        ):

            return "Autonomous Engineering Brain"

        if (

            "Execution" in text

            and "Planning" in text

        ):

            return "Engineering Automation Platform"

        if "Graph" in text:

            return "Repository Intelligence Platform"

        return "General Software Repository"

    # -------------------------------------------------

    def _engineering_type(

        self,

        identity: str,

    ) -> str:

        mapping = {

            "Autonomous Engineering Brain":
                "Engineering AI",

            "Engineering Automation Platform":
                "Automation",

            "Repository Intelligence Platform":
                "Repository Intelligence",

            "General Software Repository":
                "Software",

        }

        return mapping.get(

            identity,

            "Software",

        )

    # -------------------------------------------------

    def _confidence(

        self,

        capabilities: list[str],

    ) -> float:

        return round(

            min(

                1.0,

                0.70 + len(capabilities) * 0.03,

            ),

            2,

        )