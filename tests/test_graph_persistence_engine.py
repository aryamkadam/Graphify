from pprint import pprint

from graph_builder.engineering.engineering_graph_service import (
    EngineeringGraphService,
)

from graph_builder.engineering.engineering_workflow_engine import (
    EngineeringWorkflowEngine,
)

from graph_builder.persistence.graph_persistence_engine import (
    GraphPersistenceEngine,
)

from graph_builder.workers.engineering_task import (
    EngineeringTask,
)

print("\n========================================")
print("Graph Persistence Engine")
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

engine = GraphPersistenceEngine()

print("Save\n")
pprint(engine.save(graph_service.graph))

loaded_graph = engine.load()

print("\nLoaded Graph\n")
pprint(loaded_graph.status())