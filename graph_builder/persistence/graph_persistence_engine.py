"""
Graphify

Stage 56.1

Graph Persistence Engine

Responsible for saving and loading the
Repository Engineering Graph.

Supports backward compatibility with
older graph formats.

Author:
Graphify Core
"""

import json
from pathlib import Path

from graph_builder.graph.repository_engineering_graph import (
    RepositoryEngineeringGraph,
)
from graph_builder.graph.graph_node import GraphNode
from graph_builder.graph.graph_edge import GraphEdge


class GraphPersistenceEngine:

    VERSION = "56.1"

    def __init__(self, file_path="graphify_memory.json"):

        self.file_path = Path(file_path)

    # --------------------------------------------------

    def save(self, graph: RepositoryEngineeringGraph):

        data = {
            "nodes": [
                node.to_dict()
                for node in graph.nodes.values()
            ],
            "edges": [
                edge.to_dict()
                for edge in graph.edges.values()
            ],
            "version": self.VERSION,
        }

        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

        return {

            "status": "SAVED",

            "file": str(self.file_path),

            "version": self.VERSION,

        }

    # --------------------------------------------------

    def load(self):

        graph = RepositoryEngineeringGraph()

        if not self.file_path.exists():
            return graph

        with open(self.file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        # ----------------------------------------------
        # Load Nodes
        # ----------------------------------------------

        for node_data in data.get("nodes", []):

            node = GraphNode(

                node_type=node_data["node_type"],

                name=node_data["name"],

                metadata=node_data.get("metadata", {}),

            )

            node.node_id = node_data["node_id"]

            node.created_at = node_data["created_at"]

            graph.add_node(node)

        # ----------------------------------------------
        # Load Edges
        # Backward compatible
        # ----------------------------------------------

        for edge_data in data.get("edges", []):

            relationship = edge_data.get(

                "relationship",

                edge_data.get(

                    "relation",

                    "UNKNOWN",

                ),

            )

            edge = GraphEdge(

                source_id=edge_data["source_id"],

                target_id=edge_data["target_id"],

                relationship=relationship,

                metadata=edge_data.get("metadata", {}),

            )

            edge.edge_id = edge_data["edge_id"]

            edge.created_at = edge_data["created_at"]

            graph.add_edge(edge)

        return graph