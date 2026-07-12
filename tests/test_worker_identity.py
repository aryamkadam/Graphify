from pprint import pprint

from graph_builder.workers.worker_identity import (
    WorkerIdentity,
)

print("\n========================================")
print("Worker Identity")
print("========================================\n")

worker = WorkerIdentity(

    "Repository Architect",

    "Architecture",

)

worker.set_goal(

    "Reduce Repository Coupling"

)

worker.set_long_term_goal(

    "Evolve Repository Architecture"

)

worker.complete_task()

worker.complete_task()

print("Profile\n")

pprint(

    worker.profile()

)