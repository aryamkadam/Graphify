"""
Graphify

Stage 37.4

Graph Traversal Engine

Author:
Graphify Core
"""

from collections import deque


class GraphTraversal:

    VERSION = "37.4"

    def __init__(self, graph):

        self.graph = graph

    # ----------------------------------------

    def neighbors(self, node_id):

        neighbors = []

        for edge in self.graph.edges.values():

            if edge.source_id == node_id:

                neighbors.append(edge.target_id)

        return neighbors

    # ----------------------------------------

    def breadth_first(self, start_node):

        visited = set()

        order = []

        queue = deque([start_node])

        while queue:

            current = queue.popleft()

            if current in visited:

                continue

            visited.add(current)

            order.append(current)

            for neighbor in self.neighbors(current):

                if neighbor not in visited:

                    queue.append(neighbor)

        return order

    # ----------------------------------------

    def reachable_nodes(self, start_node):

        ids = self.breadth_first(start_node)

        return [

            self.graph.get_node(node_id)

            for node_id in ids

            if self.graph.get_node(node_id)

        ]