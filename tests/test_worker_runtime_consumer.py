from pprint import pprint

from graph_builder.runtime.worker_inbox_manager import (
    WorkerInboxManager,
)

from graph_builder.runtime.worker_runtime_consumer import (
    WorkerRuntimeConsumer,
)

print("\n========================================")
print("Worker Runtime Consumer")
print("========================================\n")

inbox = WorkerInboxManager()

consumer = WorkerRuntimeConsumer(inbox)

inbox.deliver(

    {

        "worker": "Repository Architect",

        "execution_id": "EXEC-001",

        "action": "ESCALATE",

    }

)

print("Consume\n")

pprint(

    consumer.consume(

        "Repository Architect"

    )

)

print("\nConsume Again\n")

pprint(

    consumer.consume(

        "Repository Architect"

    )

)