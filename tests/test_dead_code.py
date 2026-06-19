from graph_builder.query_engine import (
    load_symbol_index
)

from graph_builder.dead_code import (
    detect_dead_code
)

index = load_symbol_index(
    "graphify-out/symbol_index.json"
)

dead_code = detect_dead_code(
    index
)

for item in dead_code:

    print(item)