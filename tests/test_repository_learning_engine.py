from pprint import pprint

from graph_builder.repository.repository_snapshot import RepositorySnapshot
from graph_builder.repository.repository_knowledge_builder import RepositoryKnowledgeBuilder
from graph_builder.repository.repository_metrics_engine import RepositoryMetricsEngine
from graph_builder.repository.repository_evolution_engine import RepositoryEvolutionEngine
from graph_builder.repository.repository_learning_engine import RepositoryLearningEngine


def main():

    print("\n========================================")
    print("Repository Learning Engine")
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

    knowledge = RepositoryKnowledgeBuilder().build(snapshot)

    metrics = RepositoryMetricsEngine().analyze(knowledge)

    evolution = RepositoryEvolutionEngine().evolve(metrics)

    learning = RepositoryLearningEngine()

    report = learning.learn(evolution)

    print("Learning Report\n")
    pprint(report)

    print("\nRepository History\n")
    pprint(learning.history())

    print("\nSummary\n")
    pprint(learning.summary())


if __name__ == "__main__":
    main()