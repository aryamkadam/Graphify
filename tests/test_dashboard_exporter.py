from pprint import pprint

from graph_builder.query_engine import (
    load_symbol_index
)

from graph_builder.knowledge_graph import (
    build_knowledge_graph
)

from graph_builder.dashboard_exporter import (
    export_dashboard
)

symbol_index = load_symbol_index(
    "graphify-out/symbol_index.json"
)

knowledge_graph = build_knowledge_graph(
    symbol_index
)

dashboard = export_dashboard(
    symbol_index,
    knowledge_graph,
    "graphify-out/repository_dashboard.json"
)

print()

print(
    "Dashboard Exported Successfully"
)

print()

pprint(
    dashboard["health_report"]
)