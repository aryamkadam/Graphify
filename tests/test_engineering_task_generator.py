from pprint import pprint

from graph_builder.executive.executive_decision import ExecutiveDecision
from graph_builder.executive.executive_planning_engine import ExecutivePlanningEngine
from graph_builder.executive.engineering_task_generator import (
    EngineeringTaskGenerator,
)

print("\n========================================")
print("Engineering Task Generator")
print("========================================\n")

decision = ExecutiveDecision(

    decision_type="START_ENGINEERING",

    objective="Expand engineering capabilities",

    priority="HIGH",

    reasoning="Repository intelligence recommends expansion.",

    actions=["Start engineering cycle"],

)

plan = ExecutivePlanningEngine().generate_plan(decision)

tasks = EngineeringTaskGenerator().generate(plan)

print("Engineering Tasks\n")

pprint(tasks)