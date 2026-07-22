from graph_builder.runtime.worker_dispatcher import WorkerDispatcher
from graph_builder.engineering.engineering_backlog import EngineeringBacklog

print("=" * 40)
print("Worker Dispatcher")
print("=" * 40)

backlog = EngineeringBacklog()

backlog.add_task(
    title="Reduce Technical Debt",
    description="Repository-wide Refactoring",
    priority="HIGH",
)

task = backlog.next_task()

dispatcher = WorkerDispatcher()

print("\nDispatcher Status\n")
print(dispatcher.dispatcher_status())

print("\nAssignment\n")
print(dispatcher.dispatch(task))

print("\nUpdated Task\n")
print(task.to_dict())