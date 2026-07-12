from pprint import pprint

from graph_builder.executive.priority_engineering_task_queue import (
    PriorityEngineeringTaskQueue,
)

print("\n========================================")
print("Priority Engineering Task Queue")
print("========================================\n")

queue = PriorityEngineeringTaskQueue()

queue.push(

    "Refactor Runtime",

    priority=20,

)

queue.push(

    "Critical Security Fix",

    priority=100,

)

queue.push(

    "Improve UI",

    priority=40,

)

print("Status\n")

pprint(

    queue.status()

)

print("\nPeek\n")

pprint(

    queue.peek()

)

print("\nExecution Order\n")

while not queue.empty():

    pprint(

        queue.pop()

    )

print("\nFinal Status\n")

pprint(

    queue.status()

)