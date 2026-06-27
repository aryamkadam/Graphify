"""
Knowledge Graph Builder

Creates a graph representation
of repository files.

Stage 14.4
"""

import os

from graph_builder.knowledge_graph.dependency_classifier import (
    DependencyClassifier
)

from graph_builder.knowledge_graph.import_parser import ImportParser
from graph_builder.knowledge_graph.dependency_resolver import DependencyResolver


class KnowledgeGraphBuilder:

    def __init__(self, repository_path):

        self.repository_path = repository_path

    def build_nodes(self):
        """
        Every source file becomes a node.
        """

        nodes = []

        ignored_dirs = {
            "__pycache__",
            ".git",
            ".venv",
            "node_modules"
        }

        for root, dirs, files in os.walk(self.repository_path):

            dirs[:] = [
                d for d in dirs
                if d not in ignored_dirs
            ]

            for file in files:

                if file.endswith(".py"):

                    nodes.append({

                        "id": os.path.join(root, file),

                        "type": "python_file",

                        "name": file
                    })

        return nodes

    def build(self):
        """
        Build complete knowledge graph.
        """

        parser = ImportParser(
            self.repository_path
        )

        resolver = DependencyResolver(
            self.repository_path
        )

        edges = parser.parse_imports()

        resolved_edges = resolver.resolve(edges)

        return {

            "nodes": self.build_nodes(),

            "edges": resolved_edges,

            "status": "graph_created"
        }