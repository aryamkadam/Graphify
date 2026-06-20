from pprint import pprint

from graph_builder.query_engine import (
    load_symbol_index
)

from graph_builder.knowledge_graph import (
    build_knowledge_graph
)

from graph_builder.query_router import (
    route_query
)

index = load_symbol_index(
    "graphify-out/symbol_index.json"
)

graph = build_knowledge_graph(
    index
)

queries = [
    "Show dead code",
    "Show repository hotspots",
    "Show risky symbols",
    "Which function is most critical?"
]

for query in queries:

    print("\nQUERY:", query)

    result = route_query(
        query,
        index,
        graph
    )

    pprint(result[:3])