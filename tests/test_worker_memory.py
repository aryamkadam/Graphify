from pprint import pprint

from graph_builder.workers.worker_memory import (
    WorkerMemory,
)

print("\n========================================")
print("Worker Memory")
print("========================================\n")

memory = WorkerMemory()

memory.remember(

    "Architecture",

    "Repository uses plugin architecture",

)

memory.remember(

    "Architecture",

    "Avoid circular dependencies",

)

memory.remember(

    "Security",

    "JWT authentication required",

)

print("Status\n")

pprint(

    memory.status()

)

print("\nRecall All\n")

pprint(

    memory.recall()

)

print("\nArchitecture Memories\n")

pprint(

    memory.recall_category(

        "Architecture"

    )

)