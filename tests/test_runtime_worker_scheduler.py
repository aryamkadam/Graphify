from pprint import pprint

from graph_builder.executive.executive_decision import ExecutiveDecision
from graph_builder.executive.executive_planning_engine import ExecutivePlanningEngine
from graph_builder.executive.engineering_task_generator import EngineeringTaskGenerator
from graph_builder.runtime.runtime_task_dispatcher import RuntimeTaskDispatcher
from graph_builder.runtime.runtime_worker_scheduler import (
    RuntimeWorkerScheduler,
)

print("\n========================================")
print("Runtime Worker Scheduler")
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

queue = RuntimeTaskDispatcher().dispatch(tasks)

schedule = RuntimeWorkerScheduler().schedule(queue)

print("Ready Tasks\n")

pprint(schedule)