from pprint import pprint

from graph_builder.repository.repository_snapshot import RepositorySnapshot
from graph_builder.repository.repository_knowledge_builder import (
    RepositoryKnowledgeBuilder,
)
from graph_builder.repository.repository_metrics_engine import (
    RepositoryMetricsEngine,
)
from graph_builder.repository.repository_evolution_engine import (
    RepositoryEvolutionEngine,
)
from graph_builder.repository.repository_learning_engine import (
    RepositoryLearningEngine,
)
from graph_builder.repository.repository_intelligence_engine import (
    RepositoryIntelligenceEngine,
)

print("\n========================================")
print("Repository Intelligence Engine")
print("========================================\n")

snapshot = RepositorySnapshot(

    repository_name="Graphify",

    repository_path="E:/Projects/graphify",

)

snapshot.directories = [

    "graph_builder",

    "tests",

]

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

knowledge = RepositoryKnowledgeBuilder().build(snapshot)

metrics = RepositoryMetricsEngine().analyze(knowledge)

evolution = RepositoryEvolutionEngine().evolve(metrics)

learning = RepositoryLearningEngine()

learning.learn(evolution)

report = RepositoryIntelligenceEngine().analyze(

    knowledge,

    metrics,

    evolution,

    learning,

)

print("Summary\n")
pprint(report.summary())

print("\nReport\n")
pprint(report.to_dict())