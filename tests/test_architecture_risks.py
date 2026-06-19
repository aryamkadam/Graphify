from graph_builder.query_engine import (
    load_symbol_index
)

from graph_builder.architecture_risks import (
    detect_single_points_of_failure
)

index = load_symbol_index(
    "graphify-out/symbol_index.json"
)

risks = detect_single_points_of_failure(
    index
)

for risk in risks:

    print(risk)