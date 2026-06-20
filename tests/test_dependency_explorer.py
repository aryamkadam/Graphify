from pprint import pprint

from graph_builder.query_engine import (
    load_symbol_index
)

from graph_builder.knowledge_graph import (
    build_knowledge_graph
)

from graph_builder.reverse_knowledge_graph import (
    build_reverse_graph
)

from graph_builder.dependency_explorer import (
    explore_dependencies
)

index = load_symbol_index(
    "graphify-out/symbol_index.json"
)

graph = build_knowledge_graph(
    index
)

reverse_graph = build_reverse_graph(
    graph
)

tree = explore_dependencies(
    "build_repository_graph",
    reverse_graph
)

pprint(tree)