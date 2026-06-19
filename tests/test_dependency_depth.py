from graph_builder.query_engine import (
    load_symbol_index
)

from graph_builder.dependency_depth import (
    calculate_depth
)

index = load_symbol_index(
    "graphify-out/symbol_index.json"
)

print(

    calculate_depth(
        "calculate_sha256",
        index
    )

)