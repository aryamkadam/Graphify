from pprint import pprint

from graph_builder.runtime.runtime_message import RuntimeMessage
from graph_builder.workers.runtime_worker import RuntimeWorker

print("\n========================================")
print("Runtime Worker")
print("========================================\n")

worker = RuntimeWorker(

    "Repository Architect",

)

message = RuntimeMessage(

    source="Planner",

    target="Repository Architect",

    event="PLAN_READY",

)

worker.receive(

    message,

)

pprint(

    worker.status()

)