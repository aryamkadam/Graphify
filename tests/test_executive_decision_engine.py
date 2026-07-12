from pprint import pprint

from graph_builder.executive.executive_decision_engine import (
    ExecutiveDecisionEngine,
)

print("\n========================================")
print("Executive Decision Engine")
print("========================================\n")

priorities = [

    {

        "node": "Improve Security",

        "severity": "HIGH",

        "priority_score": 100,

        "recommendation": "Objective has no Sprint.",

    },

    {

        "node": "Sprint 2",

        "severity": "MEDIUM",

        "priority_score": 60,

        "recommendation": "Sprint has no Tasks.",

    },

    {

        "node": "Task X",

        "severity": "LOW",

        "priority_score": 20,

        "recommendation": "Task has no Review.",

    },

]

engine = ExecutiveDecisionEngine()

results = engine.decide(priorities)

for decision in results:

    pprint(decision)