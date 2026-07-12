from pprint import pprint

from graph_builder.engineering.engineering_workflow_engine import (
    EngineeringWorkflowEngine,
)

from graph_builder.workers.engineering_task import (
    EngineeringTask,
)

print("\n========================================")
print("Engineering Workflow Engine")
print("========================================\n")

workflow = EngineeringWorkflowEngine()

task = EngineeringTask(

    title="Implement Runtime Scheduler",

    description="Runtime scheduling engine",

)

task.complete()

result = workflow.run(task)

pprint(result)