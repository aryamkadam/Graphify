from graph_builder.repository_graph import (
    build_repository_graph
)

from graph_builder.exporter import (
    export_graph
)

graph = build_repository_graph(".")

export_graph(
    graph,
    "graphify-out"
)

print(
    f"Nodes: {len(graph['nodes'])}"
)

print(
    f"Edges: {len(graph['edges'])}"
)

print("Repository graph exported.")