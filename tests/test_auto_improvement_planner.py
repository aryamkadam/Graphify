from pprint import pprint

from graph_builder.query_engine import (
    load_symbol_index
)

from graph_builder.knowledge_graph import (
    build_knowledge_graph
)

from graph_builder.auto_improvement_planner import (
    generate_repository_plans
)

symbol_index = load_symbol_index(
    "graphify-out/symbol_index.json"
)

knowledge_graph = build_knowledge_graph(
    symbol_index
)

plans = generate_repository_plans(
    symbol_index,
    knowledge_graph
)

for plan in plans:

    print()

    pprint(plan)