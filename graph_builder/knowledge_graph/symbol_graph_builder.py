"""
Graphify

Phase 18

Symbol Graph Builder

Builds a symbol graph from the modern
SymbolExtractor output.

Responsibilities

• Build symbol nodes
• Build lightweight relationships
• Produce a normalized symbol graph

Author:
Graphify Core
"""


class SymbolGraphBuilder:

    VERSION = "P18.0"

    # --------------------------------------------------

    def build(

        self,

        symbols,

    ):

        nodes = []

        edges = []

        #
        # Build nodes
        #

        for symbol in symbols:

            if isinstance(symbol, dict):

                node = {

                    "id": symbol.get("name"),

                    "name": symbol.get("name"),

                    "type": symbol.get("type"),

                }

                nodes.append(node)

        #
        # Relationships
        #
        # Version 1:
        # No inferred edges yet.
        #

        return {

            "nodes": nodes,

            "edges": edges,

            "status": "symbol_graph_created",

            "version": self.VERSION,

        }