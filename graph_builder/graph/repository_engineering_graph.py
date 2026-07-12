"""
Graphify

Stage 37.3

Repository Engineering Graph

Author:
Graphify Core
"""

from graph_builder.graph.graph_node import GraphNode
from graph_builder.graph.graph_edge import GraphEdge


class RepositoryEngineeringGraph:

    VERSION = "37.3"

    def __init__(self):

        self.nodes = {}

        self.edges = {}

    # --------------------------------------------------

    def add_node(

        self,

        node: GraphNode,

    ):

        self.nodes[node.node_id] = node

        return node.node_id

    # --------------------------------------------------

    def add_edge(

        self,

        edge: GraphEdge,

    ):

        self.edges[edge.edge_id] = edge

        return edge.edge_id

    # --------------------------------------------------

    def get_node(

        self,

        node_id,

    ):

        return self.nodes.get(node_id)

    # --------------------------------------------------

    def get_edges_from(

        self,

        source_id,

    ):

        return [

            edge

            for edge in self.edges.values()

            if edge.source_id == source_id

        ]

    # --------------------------------------------------

    def node_count(self):

        return len(self.nodes)

    # --------------------------------------------------

    def edge_count(self):

        return len(self.edges)

    # --------------------------------------------------

    def status(self):

        return {

            "nodes": self.node_count(),

            "edges": self.edge_count(),

            "version": self.VERSION,

        }