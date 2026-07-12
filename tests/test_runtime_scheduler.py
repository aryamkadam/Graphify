from pprint import pprint

from graph_builder.scheduler.runtime_scheduler import (
    RuntimeScheduler,
)

print("\n========================================")
print("Runtime Scheduler")
print("========================================\n")

scheduler = RuntimeScheduler()

print("Queue Workers\n")

scheduler.schedule(

    "Repository Architect",

    "Analyze Repository",

)

scheduler.schedule(

    "Code Engineer",

    "Implement Runtime Scheduler",

)

scheduler.schedule(

    "Testing Engineer",

    "Validate Runtime Scheduler",

)

print("Status\n")

pprint(

    scheduler.status()

)

print("\nExecution Order\n")

while not scheduler.empty():

    pprint(

        scheduler.next()

    )

print("\nFinal Status\n")

pprint(

    scheduler.status()

)