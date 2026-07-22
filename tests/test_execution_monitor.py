from pprint import pprint

from graph_builder.runtime.execution_monitor import ExecutionMonitor
from graph_builder.engineering.engineering_backlog import EngineeringBacklog

print("=" * 40)
print("Execution Monitor")
print("=" * 40)

backlog = EngineeringBacklog()

backlog.add_task(
    title="Reduce Technical Debt",
    description="Repository-wide Refactoring",
    priority="HIGH",
)

task = backlog.next_task()
task.assigned_worker = "Code Engineer"

monitor = ExecutionMonitor()

print("\nTask Started\n")
pprint(monitor.start(task))

print("\nTask Completed\n")
pprint(monitor.complete(task))

print("\nMonitor Status\n")
pprint(monitor.monitor_status())

print("\nExecution History\n")
pprint(monitor.history())