from pprint import pprint

from graph_builder.executive.execution_repository import (
    ExecutionRepository,
)

print("\n========================================")
print("Execution Repository")
print("========================================\n")

repo = ExecutionRepository()

execution = {

    "execution_id": "EXEC-001",

    "worker": "Repository Architect",

    "status": "QUEUED",

}

repo.add(execution)

print("Single\n")

pprint(repo.get("EXEC-001"))

print("\nAll\n")

pprint(repo.all())

print("\nWorker\n")

pprint(repo.by_worker("Repository Architect"))

print("\nStatus\n")

pprint(repo.by_status("QUEUED"))

print("\nRepository Status\n")

pprint(repo.status())