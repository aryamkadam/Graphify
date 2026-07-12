from pprint import pprint

from graph_builder.engineering.engineering_workflow_engine import (
    EngineeringWorkflowEngine,
)

from graph_builder.engineering.engineering_graph_service import (
    EngineeringGraphService,
)

from graph_builder.workers.engineering_task import (
    EngineeringTask,
)

print("\n========================================")
print("Engineering Graph Service")
print("========================================\n")

workflow = EngineeringWorkflowEngine()

graph_service = EngineeringGraphService()

task = EngineeringTask(

    title="Implement Runtime Scheduler",

    description="Runtime scheduling engine",

)

task.complete()

workflow_result = workflow.run(task)

print("Graph Recording\n")

pprint(

    graph_service.record_workflow(

        workflow_result

    )

)

print("\nGraph Status\n")

pprint(

    graph_service.status()

)