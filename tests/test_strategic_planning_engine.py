from pprint import pprint

from graph_builder.persistence.graph_persistence_engine import (
    GraphPersistenceEngine,
)

from graph_builder.engineering.engineering_experience_engine import (
    EngineeringExperienceEngine,
)

from graph_builder.executive.strategic_planning_engine import (
    StrategicPlanningEngine,
)

print("\n========================================")
print("Strategic Planning Engine")
print("========================================\n")

graph = GraphPersistenceEngine().load()

experience = EngineeringExperienceEngine(graph)

planner = StrategicPlanningEngine(

    experience

)

pprint(

    planner.generate_plan()

)