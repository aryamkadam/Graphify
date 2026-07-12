from pprint import pprint

from graph_builder.runtime.runtime_event_bus import RuntimeEventBus

bus = RuntimeEventBus()


def memory_ready(payload):

    return f"Memory received {payload}"


def planner_ready(payload):

    return f"Planner received {payload}"


bus.subscribe("boot", memory_ready)
bus.subscribe("boot", planner_ready)

print("\n========================================")
print("Runtime Event Bus")
print("========================================\n")

print("Listeners\n")

pprint(bus.listeners())

print("\nEmit Event\n")

pprint(

    bus.emit(

        "boot",

        {

            "runtime": "ONLINE"

        }

    )

)