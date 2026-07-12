from pprint import pprint

from graph_builder.executive.execution_state_manager import (
    ExecutionStateManager,
)

print("\n========================================")
print("Execution State Manager")
print("========================================\n")

manager = ExecutionStateManager()

execution = {

    "execution_id": "EXEC-001",

    "worker": "Repository Architect",

    "status": "QUEUED",

}

manager.register(execution)

print("Initial\n")

pprint(manager.get("EXEC-001"))

manager.update(

    "EXEC-001",

    "RUNNING",

)

print("\nRunning\n")

pprint(manager.get("EXEC-001"))

manager.update(

    "EXEC-001",

    "COMPLETED",

)

print("\nCompleted\n")

pprint(manager.get("EXEC-001"))

print("\nSummary\n")

pprint(manager.summary())