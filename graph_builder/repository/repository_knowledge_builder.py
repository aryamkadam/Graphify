"""
Graphify

Phase 9

Stage P9.3

Repository Knowledge Builder

Transforms RepositorySnapshot into
RepositoryKnowledge.

Author:
Graphify Core
"""

from graph_builder.repository.repository_knowledge import RepositoryKnowledge


class RepositoryKnowledgeBuilder:

    VERSION = "P9.3"

    def build(
        self,
        snapshot,
    ):

        knowledge = RepositoryKnowledge(

            repository_name=snapshot.repository_name,

            repository_path=snapshot.repository_path,

        )

        # --------------------------------------------
        # Repository Structure
        # --------------------------------------------

        knowledge.directories = list(snapshot.directories)
        knowledge.files = list(snapshot.files)
        knowledge.modules = list(snapshot.modules)

        # --------------------------------------------
        # Initial Engineering Metrics
        # --------------------------------------------

        knowledge.metrics["complexity"] = "UNKNOWN"
        knowledge.metrics["maintainability"] = "UNKNOWN"
        knowledge.metrics["technical_debt"] = "UNKNOWN"
        knowledge.metrics["coverage"] = "UNKNOWN"

        return knowledge