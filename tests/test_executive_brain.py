from pprint import pprint

from graph_builder.persistence.graph_persistence_engine import (
    GraphPersistenceEngine,
)

from graph_builder.engineering.engineering_experience_engine import (
    EngineeringExperienceEngine,
)

from graph_builder.executive.executive_brain import (
    ExecutiveBrain,
)

print("\n========================================")
print("Executive Brain")
print("========================================\n")

graph = GraphPersistenceEngine().load()

experience = EngineeringExperienceEngine(graph)

brain = ExecutiveBrain(

    experience,

)

pprint(

    brain.think()

)