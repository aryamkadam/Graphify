from graph_builder.query_engine import (
    load_symbol_index
)

from graph_builder.knowledge_graph import (
    build_knowledge_graph
)

from graph_builder.refactoring_recommendations import (
    generate_recommendations
)

from graph_builder.improvement_planner import (
    build_improvement_plan
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

plan = build_improvement_plan(
    recommendations
)

for item in plan:

    print()

    print(
        f"[{item['priority']}] "
        f"{item['title']}"
    )

    for step in item["steps"]:

        print(
            f"  - {step}"
        )