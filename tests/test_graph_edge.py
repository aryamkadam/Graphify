from pprint import pprint

from graph_builder.graph.graph_node import GraphNode
from graph_builder.graph.graph_edge import GraphEdge

print("\n========================================")
print("Graph Edge")
print("========================================\n")

objective = GraphNode(

    node_type="Objective",

    name="Improve Repository Security",

)

sprint = GraphNode(

    node_type="Sprint",

    name="Sprint 1",

)

edge = GraphEdge(

    source_id=objective.node_id,

    target_id=sprint.node_id,

    relation="CONTAINS",

)

edge.update_metadata(

    "weight",

    1,

)

pprint(

    edge.to_dict()

)