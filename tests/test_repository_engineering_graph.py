from pprint import pprint

from graph_builder.graph.graph_node import GraphNode
from graph_builder.graph.graph_edge import GraphEdge
from graph_builder.graph.repository_engineering_graph import (
    RepositoryEngineeringGraph,
)

print("\n========================================")
print("Repository Engineering Graph")
print("========================================\n")

graph = RepositoryEngineeringGraph()

objective = GraphNode(

    node_type="Objective",

    name="Improve Repository Security",

)

sprint = GraphNode(

    node_type="Sprint",

    name="Sprint 1",

)

graph.add_node(objective)

graph.add_node(sprint)

edge = GraphEdge(

    source_id=objective.node_id,

    target_id=sprint.node_id,

    relation="CONTAINS",

)

graph.add_edge(edge)

print("Graph Status\n")

pprint(

    graph.status()

)

print("\nEdges From Objective\n")

for e in graph.get_edges_from(

    objective.node_id,

):

    pprint(

        e.to_dict()

)