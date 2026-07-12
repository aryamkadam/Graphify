from pprint import pprint

from graph_builder.workers.engineering_coordinator import EngineeringCoordinator
from graph_builder.workers.engineering_task import EngineeringTask

print("\n========================================")
print("Engineering Coordinator")
print("========================================\n")

coordinator = EngineeringCoordinator()

task = EngineeringTask(

    title="Implement Runtime Scheduler",

    description="Runtime scheduling system",

    priority="HIGH",

)

result = coordinator.assign(task)

pprint(result)

print("\nFinal Task\n")

pprint(task.to_dict())