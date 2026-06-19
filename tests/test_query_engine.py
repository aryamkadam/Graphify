from graph_builder.query_engine import (
    load_symbol_index,
    find_symbol
)


index = load_symbol_index(
    "graphify-out/symbol_index.json"
)

result = find_symbol(
    "scan_repository",
    index
)

print(result)