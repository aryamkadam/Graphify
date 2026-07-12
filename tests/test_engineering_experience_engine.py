from pprint import pprint

from graph_builder.engineering.engineering_graph_service import (
    EngineeringGraphService,
)

from graph_builder.engineering.engineering_experience_engine import (
    EngineeringExperienceEngine,
)

from graph_builder.engineering.engineering_workflow_engine import (
    EngineeringWorkflowEngine,
)

from graph_builder.workers.engineering_task import (
    EngineeringTask,
)

print("\n========================================")
print("Engineering Experience Engine")
print("========================================\n")

workflow = EngineeringWorkflowEngine()

graph_service = EngineeringGraphService()

task = EngineeringTask(

    title="Implement Runtime Scheduler",

    description="Runtime scheduling engine",

)

task.complete()

workflow_result = workflow.run(task)

graph_service.record_workflow(workflow_result)

engine = EngineeringExperienceEngine(

    graph_service.graph

)

print("Analysis\n")

pprint(

    engine.analyze()

)

print("\nRepository Health\n")

pprint(

    engine.repository_health()

)