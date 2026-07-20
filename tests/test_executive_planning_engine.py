from pprint import pprint

from graph_builder.executive.executive_decision import ExecutiveDecision
from graph_builder.executive.executive_planning_engine import (
    ExecutivePlanningEngine,
)

print("\n========================================")
print("Executive Planning Engine")
print("========================================\n")

decision = ExecutiveDecision(

    decision_type="START_ENGINEERING",

    objective="Expand engineering capabilities",

    priority="HIGH",

    reasoning="Repository intelligence recommends expansion.",

    actions=[

        "Start engineering cycle",

    ],

)

plan = ExecutivePlanningEngine().generate_plan(decision)

print("Engineering Plan\n")

pprint(plan)