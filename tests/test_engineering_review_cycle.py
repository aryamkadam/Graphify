from pprint import pprint

from graph_builder.workers.engineering_review_cycle import (
    EngineeringReviewCycle,
)

from graph_builder.workers.engineering_task import (
    EngineeringTask,
)

print("\n========================================")
print("Engineering Review Cycle")
print("========================================\n")

cycle = EngineeringReviewCycle()

task = EngineeringTask(

    title="Implement Runtime Scheduler",

    description="Runtime scheduling engine",

    priority="HIGH",

)

task.start()

result = cycle.execute(task)

pprint(result)

print("\nFinal Task\n")

pprint(task.to_dict())