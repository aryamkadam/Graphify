from graph_builder.query_engine import (
    load_symbol_index
)

from graph_builder.hotspot_analysis import (
    detect_hotspots
)

from graph_builder.module_hotspots import (
    detect_module_hotspots
)

index = load_symbol_index(
    "graphify-out/symbol_index.json"
)

hotspots = detect_hotspots(
    index
)

modules = detect_module_hotspots(
    hotspots
)

for module in modules:

    print(module)