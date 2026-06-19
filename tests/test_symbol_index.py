import json

from graph_builder.symbol_index import (
    build_symbol_index
)

index = build_symbol_index(".")

with open(
    "graphify-out/symbol_index.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        index,
        f,
        indent=4
    )

print(
    "Symbol index exported."
)