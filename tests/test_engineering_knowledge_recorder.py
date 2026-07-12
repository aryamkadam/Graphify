from pprint import pprint

from graph_builder.engineering.engineering_workflow_engine import (
    EngineeringWorkflowEngine,
)

from graph_builder.engineering.engineering_knowledge_recorder import (
    EngineeringKnowledgeRecorder,
)

from graph_builder.workers.engineering_task import (
    EngineeringTask,
)

print("\n========================================")
print("Engineering Knowledge Recorder")
print("========================================\n")

workflow = EngineeringWorkflowEngine()

recorder = EngineeringKnowledgeRecorder()

task = EngineeringTask(

    title="Implement Runtime Scheduler",

    description="Runtime scheduling engine",

)

task.complete()

workflow_result = workflow.run(task)

print("Workflow\n")

pprint(workflow_result)

print("\nRecord\n")

pprint(

    recorder.record(

        workflow_result

    )

)

print("\nHistory\n")

pprint(

    recorder.history()

)

print("\nStatus\n")

pprint(

    recorder.status()

)