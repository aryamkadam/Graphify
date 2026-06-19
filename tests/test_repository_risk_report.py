from pprint import pprint

from graph_builder.query_engine import (
    load_symbol_index
)

from graph_builder.repository_risk_report import (
    generate_risk_report
)

index = load_symbol_index(
    "graphify-out/symbol_index.json"
)

report = generate_risk_report(
    index
)

pprint(report)