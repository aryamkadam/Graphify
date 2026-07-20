from pprint import pprint

from graph_builder.executive.executive_decision import ExecutiveDecision
from graph_builder.executive.executive_planning_engine import ExecutivePlanningEngine
from graph_builder.executive.engineering_task_generator import EngineeringTaskGenerator
from graph_builder.runtime.runtime_task_dispatcher import RuntimeTaskDispatcher

print("\n========================================")
print("Runtime Task Dispatcher")
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

runtime_queue = RuntimeTaskDispatcher().dispatch(tasks)

print("Runtime Queue\n")

pprint(runtime_queue)