from pprint import pprint

from graph_builder.decision_history import (
    build_decision_history
)

history = build_decision_history()

print()
print("Decision History Generated")
print()

pprint(history)
