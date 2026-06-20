from graph_builder.query_engine import (
    load_symbol_index
)

from graph_builder.knowledge_graph import (
    build_knowledge_graph
)

from graph_builder.repository_assistant import (
    ask_repository
)

index = load_symbol_index(
    "graphify-out/symbol_index.json"
)

graph = build_knowledge_graph(
    index
)

queries = [
    "Which function is most critical?",
    "Show dead code",
    "Show risky symbols",
    "Show repository hotspots"
]

for query in queries:

    print("\nUSER:")

    print(query)

    print("\nGRAPHIFY:")

    print(
        ask_repository(
            query,
            index,
            graph
        )
    )