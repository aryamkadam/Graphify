from pprint import pprint

from graph_builder.decision_exporter import (
    export_decision_history
)

history = export_decision_history(
    "graphify-out/decision_history.json"
)

print()
print("Decision History Exported")
print()

pprint(history)
