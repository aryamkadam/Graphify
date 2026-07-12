from pprint import pprint

from graph_builder.executive.executive_scheduler import (
    ExecutiveScheduler,
)

print("\n========================================")
print("Executive Scheduler")
print("========================================\n")

scheduler = ExecutiveScheduler()

print("Initial Status\n")

pprint(scheduler.status())

print("\nSubmit Tasks\n")

pprint(scheduler.submit("Improve Runtime"))

pprint(scheduler.submit("Refactor Graph"))

print("\nScheduler Status\n")

pprint(scheduler.status())

print("\nDispatch\n")

pprint(scheduler.dispatch())

print("\nDispatch Again\n")

pprint(scheduler.dispatch())

print("\nDispatch Empty\n")

pprint(scheduler.dispatch())

print("\nFinal Status\n")

pprint(scheduler.status())