from pprint import pprint

from graph_builder.runtime.runtime_inbox import RuntimeInbox
from graph_builder.runtime.runtime_message import RuntimeMessage

print("\n========================================")
print("Runtime Inbox")
print("========================================\n")

inbox = RuntimeInbox()

message1 = RuntimeMessage(

    source="Memory",

    target="Planner",

    event="MEMORY_UPDATED",

)

message2 = RuntimeMessage(

    source="Executive",

    target="Planner",

    event="NEW_GOAL",

)

print("Push Messages\n")

inbox.push(message1)
inbox.push(message2)

pprint(inbox.status())

print("\nPeek\n")

pprint(inbox.peek().to_dict())

print("\nPop\n")

pprint(inbox.pop().to_dict())

print("\nInbox Status\n")

pprint(inbox.status())