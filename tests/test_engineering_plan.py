from pprint import pprint

from graph_builder.persistence.graph_persistence_engine import (
    GraphPersistenceEngine,
)

from graph_builder.engineering.engineering_experience_engine import (
    EngineeringExperienceEngine,
)

from graph_builder.executive.executive_reasoning_engine import (
    ExecutiveReasoningEngine,
)

from graph_builder.executive.engineering_planning_engine import (
    EngineeringPlanningEngine,
)

print("\n========================================")
print("Engineering Plan")
print("========================================\n")

graph = GraphPersistenceEngine().load()

experience = EngineeringExperienceEngine(graph)

reasoning = ExecutiveReasoningEngine(experience)

planner = EngineeringPlanningEngine(reasoning)

plan = planner.generate_plan()

print("Summary\n")

pprint(plan.summary())

print("\nDetails\n")

pprint(plan.details())