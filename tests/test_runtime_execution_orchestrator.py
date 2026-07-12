from pprint import pprint

from graph_builder.executive.execution_repository import (
    ExecutionRepository,
)

from graph_builder.executive.execution_state_manager import (
    ExecutionStateManager,
)

from graph_builder.runtime.runtime_execution_orchestrator import (
    RuntimeExecutionOrchestrator,
)

print("\n========================================")
print("Runtime Execution Orchestrator")
print("========================================\n")

repo = ExecutionRepository()

state = ExecutionStateManager()

execution = {

    "execution_id": "EXEC-001",

    "worker": "Repository Architect",

    "node": "Improve Security",

    "status": "QUEUED",

}

repo.add(execution)

state.register(execution)

orchestrator = RuntimeExecutionOrchestrator(

    repo,

    state,

)

results = orchestrator.dispatch()

print("Dispatch\n")

for item in results:

    pprint(item)

print("\nExecution State\n")

pprint(

    state.get("EXEC-001")

)