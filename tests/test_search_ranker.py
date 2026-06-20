from graph_builder.query_engine import (
    load_symbol_index
)

from graph_builder.semantic_search import (
    search_repository
)

from graph_builder.search_ranker import (
    rank_search_results
)

index = load_symbol_index(
    "graphify-out/symbol_index.json"
)

results = search_repository(
    "parser",
    index
)

ranked = rank_search_results(
    results,
    index
)

for item in ranked:

    print(item)