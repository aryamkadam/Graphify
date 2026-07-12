from pprint import pprint

from graph_builder.workers.testing_engineer_worker import (
    TestingEngineerWorker,
)

from graph_builder.workers.engineering_task import (
    EngineeringTask,
)

print("\n========================================")
print("Testing Engineer Worker")
print("========================================\n")

worker = TestingEngineerWorker()

task = EngineeringTask(

    title="Implement Runtime Scheduler",

    description="Runtime scheduling system",

)

task.complete()

print("Status\n")

pprint(worker.status())

print("\nThink\n")

pprint(worker.think())

print("\nValidate\n")

pprint(

    worker.validate(task)

)

print("\nFinal Status\n")

pprint(worker.status())