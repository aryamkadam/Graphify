from pprint import pprint

from graph_builder.query_engine import (
    load_symbol_index
)

from graph_builder.smart_improvement_planner import (
    generate_symbol_plan
)

index = load_symbol_index(
    "graphify-out/symbol_index.json"
)

pprint(
    generate_symbol_plan(
        "parse_python_file",
        index
    )
)