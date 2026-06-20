from graph_builder.query_engine import (
    load_symbol_index
)

from graph_builder.knowledge_graph import (
    build_knowledge_graph
)

from graph_builder.repository_qa import (
    answer_query
)

index = load_symbol_index(
    "graphify-out/symbol_index.json"
)

graph = build_knowledge_graph(
    index
)

queries = [
    "Which function is most critical?",
    "Show risky symbols",
    "Show repository hotspots",
    "Show dead code"
]

for query in queries:

    print("\n", query)

    print(
        answer_query(
            query,
            index,
            graph
        )
    )