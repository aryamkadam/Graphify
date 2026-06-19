from graph_builder.query_engine import (
    load_symbol_index
)

from graph_builder.context_pack import (
    generate_context_pack
)

index = load_symbol_index(
    "graphify-out/symbol_index.json"
)

context = generate_context_pack(
    index
)

for item in context:

    print(item)