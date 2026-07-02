"""
Graphify

Stage 20.3.3

Repository Reconstruction Engine

Reconstructs the Repository Executive Brain
from imported Graphify Repository Packages.

Author:
Graphify Core
"""

from graph_builder.executive.repository_executive_brain import (
    RepositoryExecutiveBrain,
)


class RepositoryReconstructionEngine:

    VERSION = "20.3.3"

    def __init__(self):

        self._executive_brain = RepositoryExecutiveBrain()

    # --------------------------------------------------

    def reconstruct(

        self,

        imported_context,

    ):

        """
        Unwrap translated AI context first.
        """

        repository = self._extract_repository_context(
            imported_context,
        )

        consciousness = {
            "repository_identity": repository.get(
                "repository_identity",
                {},
            )
        }

        experience = repository.get(
            "repository_story",
            {},
        )

        knowledge = repository.get(
            "repository_memory",
            {},
        )

        strategy = repository.get(
            "repository_strategy",
            {},
        )

        priorities = repository.get(
            "repository_priorities",
            {},
        )

        planner = repository.get(
            "repository_planner",
            {},
        )

        decision = repository.get(
            "repository_decision",
            {},
        )

        executive_brain = self._executive_brain.build(

            consciousness,

            experience,

            knowledge,

            strategy,

            priorities,

            planner,

            decision,

        )

        return {

            "repository_executive_brain": executive_brain,

            "repository_ready": True,

            "continuation_ready": True,

            "reconstructed": True,

            "version": self.VERSION,

        }

    # --------------------------------------------------

    def _extract_repository_context(

        self,

        imported_context,

    ):

        """
        Supports every Graphify AI translator.

        ChatGPT  -> memory
        Claude   -> repository_context
        Gemini   -> engineering_context
        Generic  -> context
        """

        for key in (

            "memory",

            "repository_context",

            "engineering_context",

            "context",

        ):

            if key in imported_context:

                return imported_context[key]

        return imported_context