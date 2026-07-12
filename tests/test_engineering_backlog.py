from pprint import pprint

from graph_builder.engineering.engineering_backlog import (
    EngineeringBacklog,
)

print("\n========================================")
print("Engineering Backlog")
print("========================================\n")

backlog = EngineeringBacklog()

backlog.add_task(

    "Implement Runtime Scheduler",

    "Runtime scheduling engine",

    priority="HIGH",

)

backlog.add_task(

    "Improve Documentation",

    "Update architecture docs",

    priority="LOW",

)

backlog.add_task(

    "Security Audit",

    "Review runtime security",

    priority="HIGH",

)

print("Backlog Status\n")

pprint(backlog.status())

print("\nNext Task\n")

task = backlog.next_task()

pprint(task.to_dict())