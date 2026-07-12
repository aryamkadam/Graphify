from pprint import pprint

from graph_builder.workers.repository_architect_worker import (
    RepositoryArchitectWorker,
)

print("\n========================================")
print("Repository Architect Worker")
print("========================================\n")

worker = RepositoryArchitectWorker()

print("Status")

pprint(worker.status())

print("\nThink")

pprint(worker.think())

print("\nExecute")

pprint(worker.execute())

brain = {

    "identity": {

        "phase": "Stabilization",

        "technical_direction": "Positive",

    }

}

print("\nRecommendation")

pprint(

    worker.recommend(

        brain,

    )

)