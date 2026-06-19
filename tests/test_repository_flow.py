from graph_builder.query_engine import (
    load_symbol_index
)

from graph_builder.repository_flow import (
    build_repository_flow
)

index = load_symbol_index(
    "graphify-out/symbol_index.json"
)

flow = build_repository_flow(
    "calculate_sha256",
    index
)

print(flow)