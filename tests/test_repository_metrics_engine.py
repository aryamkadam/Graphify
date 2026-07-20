from pprint import pprint

from graph_builder.repository.repository_snapshot import RepositorySnapshot
from graph_builder.repository.repository_knowledge_builder import (
    RepositoryKnowledgeBuilder,
)
from graph_builder.repository.repository_metrics_engine import (
    RepositoryMetricsEngine,
)


def main():

    print("\n========================================")
    print("Repository Metrics Engine")
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

        "repository.py",

        "planner.py",

    ]

    snapshot.modules = [

        "runtime",

        "repository",

    ]

    builder = RepositoryKnowledgeBuilder()

    knowledge = builder.build(snapshot)

    metrics = RepositoryMetricsEngine().analyze(

        knowledge

    )

    pprint(metrics)


if __name__ == "__main__":
    main()