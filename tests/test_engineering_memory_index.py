from pprint import pprint

from graph_builder.memory.engineering_memory import EngineeringMemory
from graph_builder.workers.engineering_review_cycle import EngineeringReviewCycle
from graph_builder.workers.engineering_task import EngineeringTask

print("\n========================================")
print("Engineering Memory Index")
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

memory.remember(review)

print("Status\n")

pprint(memory.status())

print("\nSearch Title\n")

pprint(

    memory.find_by_title(

        "Implement Runtime Scheduler",

    )

)

print("\nSearch Worker\n")

pprint(

    memory.find_by_worker(

        "Code Engineer",

    )

)

print("\nSearch Status\n")

pprint(

    memory.find_by_status(

        "COMPLETED",

    )

)