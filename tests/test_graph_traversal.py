from pprint import pprint

from graph_builder.graph.graph_node import GraphNode
from graph_builder.graph.graph_edge import GraphEdge
from graph_builder.graph.repository_engineering_graph import (
    RepositoryEngineeringGraph,
)
from graph_builder.graph.graph_traversal import (
    GraphTraversal,
)

print("\n========================================")
print("Graph Traversal")
print("========================================\n")

graph = RepositoryEngineeringGraph()

objective = GraphNode("Objective", "Security")

sprint = GraphNode("Sprint", "Sprint 1")

task = GraphNode("Task", "Refactor Login")

graph.add_node(objective)
graph.add_node(sprint)
graph.add_node(task)

graph.add_edge(
    GraphEdge(
        objective.node_id,
        sprint.node_id,
        "CONTAINS",
    )
)

graph.add_edge(
    GraphEdge(
        sprint.node_id,
        task.node_id,
        "CONTAINS",
    )
)

traversal = GraphTraversal(graph)

print("Reachable Nodes\n")

for node in traversal.reachable_nodes(
    objective.node_id
):
    pprint(node.to_dict())