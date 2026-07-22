from pprint import pprint

from graph_builder.runtime.feedback_collector import FeedbackCollector
from graph_builder.runtime.learning_integrator import LearningIntegrator
from graph_builder.engineering.engineering_backlog import EngineeringBacklog

print("=" * 40)
print("Learning Integrator")
print("=" * 40)

backlog = EngineeringBacklog()

backlog.add_task(
    title="Reduce Technical Debt",
    description="Repository-wide Refactoring",
    priority="HIGH",
)

task = backlog.next_task()
task.assigned_worker = "Code Engineer"

collector = FeedbackCollector()

feedback = collector.collect(

    task,

    success=True,

    summary="Repository refactoring completed successfully.",

    metrics={

        "files_modified": 18,

        "warnings_removed": 6,

    },

)

integrator = LearningIntegrator()

print("\nIntegrating\n")
pprint(integrator.integrate(feedback))

print("\nExperience Memory\n")
pprint(integrator.experience())

print("\nStatus\n")
pprint(integrator.status())