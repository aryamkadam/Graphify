from pprint import pprint

from graph_builder.workers.base_worker import (
    BaseWorker,
)

print("\n========================================")
print("Base Worker")
print("========================================\n")

worker = BaseWorker(

    "Repository Architect"

)

print("Think\n")

pprint(

    worker.think()

)

print("\nExecute\n")

pprint(

    worker.execute(

        "Refactor Login"

    )

)

print("\nReport\n")

pprint(

    worker.report()

)