from graph_builder.query_engine import (
    load_symbol_index
)

from graph_builder.knowledge_graph import (
    build_knowledge_graph
)

from graph_builder.reverse_knowledge_graph import (
    build_reverse_graph
)

symbol_index = load_symbol_index(
    "graphify-out/symbol_index.json"
)

graph = build_knowledge_graph(
    symbol_index
)

reverse_graph = build_reverse_graph(
    graph
)

for symbol, dependencies in reverse_graph.items():

    print()

    print(symbol)

    for dependency in dependencies:

        print(
            f"  -> {dependency}"
        )