from pprint import pprint

from graph_builder.query_engine import (
    load_symbol_index
)

from graph_builder.knowledge_graph import (
    build_knowledge_graph
)

from graph_builder.repository_health_report import (
    generate_health_report
)

symbol_index = load_symbol_index(
    "graphify-out/symbol_index.json"
)

knowledge_graph = build_knowledge_graph(
    symbol_index
)

report = generate_health_report(
    symbol_index,
    knowledge_graph
)

pprint(
    report
)