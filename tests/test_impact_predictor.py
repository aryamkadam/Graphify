from graph_builder.query_engine import (
    load_symbol_index
)

from graph_builder.knowledge_graph import (
    build_knowledge_graph
)

from graph_builder.impact_predictor import (
    predict_impact
)

index = load_symbol_index(
    "graphify-out/symbol_index.json"
)

graph = build_knowledge_graph(
    index
)

impacted = predict_impact(
    "parse_python_file",
    graph
)

for item in impacted:

    print(item)