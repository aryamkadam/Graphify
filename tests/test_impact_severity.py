from graph_builder.query_engine import (
    load_symbol_index
)

from graph_builder.knowledge_graph import (
    build_knowledge_graph
)

from graph_builder.impact_severity import (
    calculate_impact_severity
)

index = load_symbol_index(
    "graphify-out/symbol_index.json"
)

graph = build_knowledge_graph(
    index
)

for symbol in [
    "parse_python_file",
    "calculate_sha256",
    "find_duplicates",
    "build_graph"
]:

    result = calculate_impact_severity(
        symbol,
        graph
    )

    print(result)