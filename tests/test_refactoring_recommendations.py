from graph_builder.query_engine import (
    load_symbol_index
)

from graph_builder.knowledge_graph import (
    build_knowledge_graph
)

from graph_builder.refactoring_recommendations import (
    generate_recommendations
)

symbol_index = load_symbol_index(
    "graphify-out/symbol_index.json"
)

knowledge_graph = build_knowledge_graph(
    symbol_index
)

recommendations = (
    generate_recommendations(
        symbol_index,
        knowledge_graph
    )
)

print()

print(
    "REPOSITORY IMPROVEMENT PLAN"
)

print(
    "=" * 40
)

for recommendation in recommendations:

    print()

    print(
        f"[{recommendation['priority']}] "
        f"(score={recommendation['score']})"
    )

    print(
        recommendation["message"]
    )