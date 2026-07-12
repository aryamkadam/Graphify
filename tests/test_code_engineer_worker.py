from pprint import pprint

from graph_builder.workers.code_engineer_worker import (
    CodeEngineerWorker,
)

print("\n========================================")
print("Code Engineer Worker")
print("========================================\n")

worker = CodeEngineerWorker()

print("Status")

pprint(worker.status())

print("\nThink")

pprint(worker.think())

print("\nExecute")

pprint(

    worker.execute(

        "Runtime Scheduler"

    )

)

print("\nReport")

pprint(

    worker.report()

)