from graph_builder.query_engine import (
    load_symbol_index
)

from graph_builder.god_file_detector import (
    detect_god_files
)

index = load_symbol_index(
    "graphify-out/symbol_index.json"
)

results = detect_god_files(
    index
)

for item in results:

    print(item)