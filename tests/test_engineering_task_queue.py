from pprint import pprint

from graph_builder.executive.engineering_task_queue import (
    EngineeringTaskQueue,
)

print("\n========================================")
print("Engineering Task Queue")
print("========================================\n")

queue = EngineeringTaskQueue()

print("Initial Status\n")

pprint(queue.status())

print("\nPush Tasks\n")

queue.push("Refactor Runtime")

queue.push("Improve Scheduler")

queue.push("Optimize Graph")

pprint(queue.status())

print("\nPeek\n")

pprint(queue.peek())

print("\nPop\n")

pprint(queue.pop())

print("\nQueue Status\n")

pprint(queue.status())

print("\nRemaining\n")

while not queue.empty():

    pprint(queue.pop())

print("\nFinal Status\n")

pprint(queue.status())