from pprint import pprint

from graph_builder.decision_engine import (
    create_decision
)


decision = create_decision(

    title=
    "Repository Brain Introduced",

    reason=
    "Need single source of truth for AI context transfer",

    impact=
    "repository_brain.json generated",

    stage=
    "stage-6.1-stable",

    commit=
    "fc4e2b3"
)

print()
print("Decision Engine Working")
print()

pprint(
    decision
)