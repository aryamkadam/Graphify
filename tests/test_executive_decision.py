from pprint import pprint

from graph_builder.executive.executive_decision import (
    ExecutiveDecision,
)

print("\n========================================")
print("Executive Decision")
print("========================================\n")

decision = ExecutiveDecision(

    decision_type="START_ENGINEERING",

    objective="Expand engineering capabilities",

    priority="HIGH",

    reasoning=(
        "Repository intelligence recommends "
        "engineering expansion."
    ),

    actions=[

        "Start engineering cycle",

        "Assign Planning Worker",

        "Assign Code Engineer",

    ],

)

print("Summary\n")
pprint(decision.summary())

print("\nDecision\n")
pprint(decision.to_dict())