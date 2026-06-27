from graph_builder.analyzer.repository import (
    RepositoryAnalyzer
)
"""
Graphify Engine

Central orchestration layer for Graphify.

The SDK interacts only with this engine.
"""

from graph_builder.context.builder import (
    build_context
)

from graph_builder.protocols.uacp.builder import (
    build_uacp
)
from graph_builder.analyzer.repository import (
    RepositoryAnalyzer
)


class GraphifyEngine:

    def context(self):
        """
        Return the canonical Graphify Context.
        """
        return build_context()

    def export_uacp(self):
        """
        Export the current Graphify Context
        as UACP.
        """
        context = build_context()

        return build_uacp(context)
    def analyze_repository(self, repository_path):

        analyzer = RepositoryAnalyzer(
        repository_path
    )

        return analyzer.analyze()