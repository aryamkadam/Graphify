from graph_builder.query_engine import (
    load_symbol_index
)

from graph_builder.criticality_score import (
    calculate_criticality
)

index = load_symbol_index(
    "graphify-out/symbol_index.json"
)

results = calculate_criticality(
    index
)

for item in results[:10]:

    print(item)