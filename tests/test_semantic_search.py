from graph_builder.query_engine import (
    load_symbol_index
)

from graph_builder.semantic_search import (
    search_repository
)

index = load_symbol_index(
    "graphify-out/symbol_index.json"
)

queries = [

    "hashing",
    "parsing",
    "duplicate",
    "scanner",
    "report"

]

for query in queries:

    print()

    print(
        f"QUERY: {query}"
    )

    results = search_repository(
        query,
        index
    )

    for result in results[:5]:

        print(result)