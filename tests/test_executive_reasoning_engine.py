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

print("\n========================================")
print("Executive Reasoning Engine")
print("========================================\n")

graph = GraphPersistenceEngine().load()

experience = EngineeringExperienceEngine(graph)

engine = ExecutiveReasoningEngine(

    experience,

)

pprint(

    engine.reason()

)