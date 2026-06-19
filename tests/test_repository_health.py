from pprint import pprint

from graph_builder.query_engine import (
    load_symbol_index
)

from graph_builder.repository_health import (
    generate_executive_summary
)

index = load_symbol_index(
    "graphify-out/symbol_index.json"
)

result = generate_executive_summary(
    index
)

pprint(result)