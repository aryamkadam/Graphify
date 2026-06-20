from graph_builder.query_engine import (
    load_symbol_index
)

from graph_builder.knowledge_graph import (
    build_knowledge_graph
)

from graph_builder.critical_symbol_ranking import (
    rank_critical_symbols
)

index = load_symbol_index(
    "graphify-out/symbol_index.json"
)

graph = build_knowledge_graph(
    index
)

rankings = rank_critical_symbols(
    index,
    graph
)

for item in rankings[:10]:

    print(item)