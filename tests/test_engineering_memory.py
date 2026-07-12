from pprint import pprint

from graph_builder.memory.engineering_memory import EngineeringMemory
from graph_builder.workers.engineering_review_cycle import EngineeringReviewCycle
from graph_builder.workers.engineering_task import EngineeringTask

print("\n========================================")
print("Engineering Memory")
print("========================================\n")

memory = EngineeringMemory()

cycle = EngineeringReviewCycle()

task = EngineeringTask(

    title="Implement Runtime Scheduler",

    description="Runtime scheduling engine",

    priority="HIGH",

)

task.start()

review = cycle.execute(task)

print("Store Review\n")

pprint(

    memory.remember(review)

)

print("\nMemory Status\n")

pprint(

    memory.status()

)

print("\nLatest Entry\n")

pprint(

    memory.latest()

)