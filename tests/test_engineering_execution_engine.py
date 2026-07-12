from pprint import pprint

from graph_builder.runtime.runtime_brain import RuntimeBrain

from graph_builder.executive.executive_reasoning_engine import (
    ExecutiveReasoningEngine,
)

from graph_builder.executive.engineering_planning_engine import (
    EngineeringPlanningEngine,
)

from graph_builder.executive.engineering_execution_engine import (
    EngineeringExecutionEngine,
)

print("\n========================================")
print("Engineering Execution Engine")
print("========================================\n")

brain = RuntimeBrain()

reasoning = ExecutiveReasoningEngine(

    brain.experience,

)

planner = EngineeringPlanningEngine(

    reasoning,

)

plan = planner.generate_plan()

executor = EngineeringExecutionEngine(

    brain.registry,

)

pprint(

    executor.execute(plan)

)