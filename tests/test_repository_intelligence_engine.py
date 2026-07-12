from pprint import pprint

from graph_builder.runtime.runtime_brain import RuntimeBrain
from graph_builder.repository.repository_intelligence_engine import (
    RepositoryIntelligenceEngine,
)

print("\n========================================")
print("Repository Intelligence Engine")
print("========================================\n")

brain = RuntimeBrain()

engine = RepositoryIntelligenceEngine(

    brain.graph,

)

pprint(

    engine.analyze()

)