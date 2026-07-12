from pprint import pprint

from graph_builder.graph.graph_node import GraphNode

print("\n========================================")
print("Graph Node")
print("========================================\n")

node = GraphNode(

    node_type="Objective",

    name="Improve Repository Security",

)

node.update_metadata(

    "priority",

    "HIGH",

)

node.update_metadata(

    "owner",

    "Executive Brain",

)

pprint(

    node.to_dict()

)