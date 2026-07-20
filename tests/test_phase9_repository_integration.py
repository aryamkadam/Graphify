"""
Graphify

Phase 9

Repository Intelligence Integration Test

Validates the complete Repository
Intelligence Pipeline.

P9.1 -> P9.7

Author:
Graphify Core
"""

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


def main():

    print("\n========================================")
    print("PHASE 9 REPOSITORY INTEGRATION")
    print("========================================\n")

    results = {}

    # ------------------------------------------
    # Repository Snapshot
    # ------------------------------------------

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

    snapshot.directory_count = len(snapshot.directories)
    snapshot.file_count = len(snapshot.files)
    snapshot.module_count = len(snapshot.modules)

    results["Repository Snapshot"] = True

    # ------------------------------------------
    # Knowledge Builder
    # ------------------------------------------

    knowledge = RepositoryKnowledgeBuilder().build(snapshot)

    results["Knowledge Builder"] = True

    # ------------------------------------------
    # Metrics Engine
    # ------------------------------------------

    metrics = RepositoryMetricsEngine().analyze(knowledge)

    results["Metrics Engine"] = True

    # ------------------------------------------
    # Evolution Engine
    # ------------------------------------------

    evolution = RepositoryEvolutionEngine().evolve(metrics)

    results["Evolution Engine"] = True

    # ------------------------------------------
    # Learning Engine
    # ------------------------------------------

    learning = RepositoryLearningEngine()

    learning.learn(evolution)

    results["Learning Engine"] = True

    # ------------------------------------------
    # Intelligence Engine
    # ------------------------------------------

    report = RepositoryIntelligenceEngine().analyze(

        knowledge,

        metrics,

        evolution,

        learning,

    )

    results["Repository Intelligence"] = True

    # ------------------------------------------

    pprint(results)

    print("\n----------------------------------------")

    overall = all(results.values())

    print("Overall Status :", "PASS" if overall else "FAIL")

    print("----------------------------------------")

    print("\nRepository Intelligence Report\n")

    pprint(report.to_dict())


if __name__ == "__main__":
    main()