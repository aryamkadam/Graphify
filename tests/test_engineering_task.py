from pprint import pprint

from graph_builder.workers.engineering_task import EngineeringTask

print("\n========================================")
print("Engineering Task")
print("========================================\n")

task = EngineeringTask(

    title="Implement Runtime Scheduler",

    description="Create runtime scheduler service",

    priority="HIGH",

)

print("Created\n")

pprint(task.to_dict())

task.assign("Code Engineer")

print("\nAssigned\n")

pprint(task.to_dict())

task.start()

print("\nStarted\n")

pprint(task.to_dict())

task.complete()

print("\nCompleted\n")

pprint(task.to_dict())