"""
Graphify

Phase 3

Stage P3.11

Repository Intelligence Engine

Analyzes repository engineering metrics
to support Executive decisions.

Author:
Graphify Core
"""


class RepositoryIntelligenceEngine:

    VERSION = "P3.11"

    def __init__(

        self,

        graph,

    ):

        self.graph = graph

    # --------------------------------------------------

    def analyze(self):

        nodes = self.graph.node_count()

        edges = self.graph.edge_count()

        return {

            "repository_size": nodes,

            "relationships": edges,

            "complexity":

                self._complexity(nodes, edges),

            "growth":

                self._growth(nodes),

            "version":

                self.VERSION,

        }

    # --------------------------------------------------

    def _complexity(

        self,

        nodes,

        edges,

    ):

        if nodes == 0:

            return "EMPTY"

        ratio = edges / nodes

        if ratio < 1:

            return "LOW"

        elif ratio < 2:

            return "MODERATE"

        else:

            return "HIGH"

    # --------------------------------------------------

    def _growth(

        self,

        nodes,

    ):

        if nodes < 20:

            return "EARLY"

        elif nodes < 100:

            return "GROWING"

        else:

            return "MATURE"