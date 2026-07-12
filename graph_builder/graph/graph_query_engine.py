"""
Graphify

Stage 37.5

Repository Graph Query Engine

Author:
Graphify Core
"""


class GraphQueryEngine:

    VERSION = "37.5"

    def __init__(self, graph):

        self.graph = graph

    # ------------------------------------------

    def by_node_type(

        self,

        node_type,

    ):

        return [

            node

            for node in self.graph.nodes.values()

            if node.node_type == node_type

        ]

    # ------------------------------------------

    def by_name(

        self,

        name,

    ):

        return [

            node

            for node in self.graph.nodes.values()

            if node.name == name

        ]

    # ------------------------------------------

    def by_relation(

        self,

        relation,

    ):

        return [

            edge

            for edge in self.graph.edges.values()

            if edge.relation == relation

        ]

    # ------------------------------------------

    def statistics(self):

        return {

            "nodes": len(self.graph.nodes),

            "edges": len(self.graph.edges),

            "version": self.VERSION,

        }