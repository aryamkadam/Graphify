from pprint import pprint

from graph_builder.runtime.runtime_message_bus import (
    RuntimeMessageBus,
)

print("\n========================================")
print("Runtime Message Bus")
print("========================================\n")

bus = RuntimeMessageBus()

bus.publish(

    {

        "worker": "Repository Architect",

        "execution_id": "EXEC-001",

        "action": "ESCALATE",

    }

)

bus.publish(

    {

        "worker": "Planner",

        "execution_id": "EXEC-002",

        "action": "PLAN",

    }

)

print("Status\n")

pprint(bus.status())

print("\nConsume 1\n")

pprint(bus.consume())

print("\nConsume 2\n")

pprint(bus.consume())

print("\nFinal Status\n")

pprint(bus.status())