from pprint import pprint

from graph_builder.runtime.feedback_collector import FeedbackCollector
from graph_builder.engineering.engineering_backlog import EngineeringBacklog

print("=" * 40)
print("Feedback Collector")
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

        "technical_debt_reduction": "High",

    }

)

print("\nCollected Feedback\n")
pprint(feedback)

print("\nCollector Status\n")
pprint(collector.collector_status())

print("\nFeedback History\n")
pprint(collector.history())