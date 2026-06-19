from graph_builder.query_engine import (
    load_symbol_index
)

from graph_builder.hotspot_analysis import (
    detect_hotspots
)

index = load_symbol_index(
    "graphify-out/symbol_index.json"
)

hotspots = detect_hotspots(
    index
)

for hotspot in hotspots:

    print(hotspot)