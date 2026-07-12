from pprint import pprint

from graph_builder.reasoning.engineering_priority_engine import (
    EngineeringPriorityEngine,
)

print("\n========================================")
print("Engineering Priority Engine")
print("========================================\n")

recommendations = [

    {
        "node": "Improve Security",
        "severity": "HIGH",
        "recommendation": "Objective has no Sprint.",
    },

    {
        "node": "Sprint 2",
        "severity": "MEDIUM",
        "recommendation": "Sprint has no Tasks.",
    },

    {
        "node": "Task X",
        "severity": "LOW",
        "recommendation": "Task has no Review.",
    },

]

engine = EngineeringPriorityEngine()

results = engine.prioritize(
    recommendations
)

for r in results:

    pprint(r)