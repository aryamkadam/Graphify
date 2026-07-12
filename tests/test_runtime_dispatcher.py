from pprint import pprint

from graph_builder.runtime.runtime_dispatcher import RuntimeDispatcher
from graph_builder.runtime.runtime_message import RuntimeMessage
from graph_builder.runtime.runtime_service import RuntimeService


class PlannerService(RuntimeService):

    def __init__(self):

        super().__init__(

            "Planner",

        )

        self.messages = []

    def receive_message(

        self,

        message,

    ):

        self.messages.append(

            message,

        )


dispatcher = RuntimeDispatcher()

planner = PlannerService()

dispatcher.register(

    planner,

)

message = RuntimeMessage(

    source="Memory Plugin",

    target="Planner",

    event="MEMORY_UPDATED",

    payload={

        "nodes": 152,

    },

)

print("\n========================================")
print("Runtime Dispatcher")
print("========================================\n")

pprint(

    dispatcher.dispatch(

        message,

    )

)

print("\nPlanner Inbox\n")

for msg in planner.messages:

    pprint(

        msg.to_dict()

    )