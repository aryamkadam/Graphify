from pprint import pprint

from graph_builder.workers.worker_registry import WorkerRegistry

from graph_builder.workers.repository_architect_worker import RepositoryArchitectWorker
from graph_builder.workers.code_engineer_worker import CodeEngineerWorker
from graph_builder.workers.testing_engineer_worker import TestingEngineerWorker

from graph_builder.workers.worker_evolution_engine import (
    WorkerEvolutionEngine,
)

print("\n========================================")
print("Worker Evolution Engine")
print("========================================\n")

registry = WorkerRegistry()

registry.register(

    RepositoryArchitectWorker()

)

registry.register(

    CodeEngineerWorker()

)

registry.register(

    TestingEngineerWorker()

)

execution_report = {

    "report": [

        {

            "worker":

                "Repository Architect"

        },

        {

            "worker":

                "Code Engineer"

        },

        {

            "worker":

                "Testing Engineer"

        }

    ]

}

engine = WorkerEvolutionEngine(

    registry

)

pprint(

    engine.evolve(

        execution_report

    )

)

print("\nUpdated Profiles\n")

for worker_name in registry.all_workers():

    worker = registry.get(

        worker_name

    )

    pprint(

        worker.identity.profile()

    )