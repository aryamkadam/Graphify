from pprint import pprint

from graph_builder.kernel.engineering_kernel import (
    EngineeringKernel,
)

from graph_builder.workers.engineering_task import (
    EngineeringTask,
)

print("\n========================================")
print("Engineering Kernel")
print("========================================\n")

kernel = EngineeringKernel()

task = EngineeringTask(

    title="Implement Runtime Scheduler",

    description="Runtime scheduling engine",

    priority="HIGH",

)

task.start()

print("Kernel Status\n")

pprint(

    kernel.status()

)

print("\nExecute\n")

result = kernel.execute(task)

pprint(result)