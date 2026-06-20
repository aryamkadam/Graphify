from graph_builder.query_engine import (
    load_symbol_index
)

from graph_builder.knowledge_graph import (
    build_knowledge_graph
)

symbol_index = load_symbol_index(
    "graphify-out/symbol_index.json"
)

graph = build_knowledge_graph(
    symbol_index
)

for symbol, connections in graph.items():

    if connections:

        print()

        print(
            f"{symbol}"
        )

        for connection in connections:

            print(
                f"  -> {connection}"
            )