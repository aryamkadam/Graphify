from pprint import pprint

from graph_builder.runtime.worker_inbox_manager import (
    WorkerInboxManager,
)

print("\n========================================")
print("Worker Inbox Manager")
print("========================================\n")

manager = WorkerInboxManager()

manager.deliver(
    {
        "worker": "Repository Architect",
        "execution_id": "EXEC-001",
        "action": "ESCALATE",
    }
)

manager.deliver(
    {
        "worker": "Testing Engineer",
        "execution_id": "EXEC-002",
        "action": "VERIFY",
    }
)

manager.deliver(
    {
        "worker": "Repository Architect",
        "execution_id": "EXEC-003",
        "action": "REVIEW",
    }
)

print("Inbox Status\n")
pprint(manager.status())

print("\nRepository Architect receives\n")
pprint(manager.receive("Repository Architect"))

print("\nRepository Architect receives again\n")
pprint(manager.receive("Repository Architect"))

print("\nTesting Engineer receives\n")
pprint(manager.receive("Testing Engineer"))

print("\nFinal Status\n")
pprint(manager.status())