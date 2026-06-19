from graph_builder.query_engine import (
    load_symbol_index
)

from graph_builder.impact_analysis import (
    analyze_impact
)

index = load_symbol_index(
    "graphify-out/symbol_index.json"
)

result = analyze_impact(
    "calculate_sha256",
    index
)

print(result)