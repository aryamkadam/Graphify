from graph_builder.query_engine import (
    load_symbol_index
)

from graph_builder.knowledge_graph import (
    build_knowledge_graph
)

from graph_builder.risk_ranking import (
    rank_repository_risks
)

index = load_symbol_index(
    "graphify-out/symbol_index.json"
)

graph = build_knowledge_graph(
    index
)

rankings = rank_repository_risks(
    index,
    graph
)

for item in rankings[:10]:

    print(item)
    