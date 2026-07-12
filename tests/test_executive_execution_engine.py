from pprint import pprint

from graph_builder.executive.executive_execution_engine import (
    ExecutiveExecutionEngine,
)

print("\n========================================")
print("Executive Execution Engine")
print("========================================\n")

decisions = [

    {

        "node": "Improve Security",

        "action": "ESCALATE",

        "assigned_worker": "Repository Architect",

        "priority_score": 100,

    },

    {

        "node": "Sprint 2",

        "action": "PLAN",

        "assigned_worker": "Planner",

        "priority_score": 60,

    },

]

engine = ExecutiveExecutionEngine()

print("Execute\n")

results = engine.execute(decisions)

for result in results:

    pprint(result)

print("\nHistory\n")

for item in engine.history():

    pprint(item)

print("\nStatus\n")

pprint(engine.status())