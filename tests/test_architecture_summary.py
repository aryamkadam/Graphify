from graph_builder.query_engine import (
    load_symbol_index
)

from graph_builder.architecture_exporter import (
    export_architecture_summary
)

symbol_index = load_symbol_index(
    "graphify-out/symbol_index.json"
)

summary = (
    export_architecture_summary(
        symbol_index,
        "graphify-out/architecture_summary.md"
    )
)

print()

print(
    "Architecture Summary Generated"
)

print()

print(
    summary
)