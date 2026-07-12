from pprint import pprint

from graph_builder.runtime.runtime_message import RuntimeMessage

print("\n========================================")
print("Runtime Message")
print("========================================\n")

message = RuntimeMessage(

    source="Memory Plugin",

    target="Planner",

    event="MEMORY_UPDATED",

    payload={

        "nodes": 152,

        "edges": 410,

    },

)

pprint(message.to_dict())

print()

print(message.summary())