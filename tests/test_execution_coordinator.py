from graph_builder.runtime.execution_coordinator import ExecutionCoordinator
from graph_builder.engineering.engineering_backlog import EngineeringBacklog

print("=" * 40)
print("Execution Coordinator")
print("=" * 40)

backlog = EngineeringBacklog()

backlog.add_task(
    title="Reduce Technical Debt",
    description="Repository-wide Refactoring",
    priority="HIGH",
)

coordinator = ExecutionCoordinator(backlog)

print("\nCoordinator Status\n")
print(coordinator.coordinator_status())

print("\nNext Task\n")
task = coordinator.execution_ready()

if task:
    print(task.to_dict())
else:
    print(None)