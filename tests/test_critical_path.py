from graph_builder.query_engine import (
    load_symbol_index
)

from graph_builder.critical_path import (
    detect_critical_symbols
)

index = load_symbol_index(
    "graphify-out/symbol_index.json"
)

critical = detect_critical_symbols(
    index
)

for item in critical:

    print(item)