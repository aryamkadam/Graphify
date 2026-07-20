from pprint import pprint

from graph_builder.repository.repository_snapshot import RepositorySnapshot
from graph_builder.repository.repository_knowledge_builder import RepositoryKnowledgeBuilder
from graph_builder.repository.repository_metrics_engine import RepositoryMetricsEngine
from graph_builder.repository.repository_evolution_engine import RepositoryEvolutionEngine
from graph_builder.repository.repository_learning_engine import RepositoryLearningEngine
from graph_builder.repository.repository_intelligence_engine import RepositoryIntelligenceEngine

from graph_builder.executive.engineering_executive_brain import (
    EngineeringExecutiveBrain,
)

print("\n========================================")
print("Engineering Executive Brain")
print("========================================\n")

snapshot = RepositorySnapshot(

    repository_name="Graphify",

    repository_path="E:/Projects/graphify",

)

snapshot.directories = ["graph_builder", "tests"]

snapshot.files = [

    "main.py",

    "runtime.py",

    "planner.py",

    "repository.py",

]

snapshot.modules = [

    "runtime",

    "repository",

]

snapshot.directory_count = len(snapshot.directories)
snapshot.file_count = len(snapshot.files)
snapshot.module_count = len(snapshot.modules)

knowledge = RepositoryKnowledgeBuilder().build(snapshot)

metrics = RepositoryMetricsEngine().analyze(knowledge)

evolution = RepositoryEvolutionEngine().evolve(metrics)

learning = RepositoryLearningEngine()

learning.learn(evolution)

intelligence = RepositoryIntelligenceEngine().analyze(

    knowledge,

    metrics,

    evolution,

    learning,

)

decision = EngineeringExecutiveBrain().think(intelligence)

print("Decision Summary\n")
pprint(decision.summary())

print("\nExecutive Decision\n")
pprint(decision.to_dict())