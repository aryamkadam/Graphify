from pprint import pprint

from graph_builder.decision.engineering_decision_engine import (
    EngineeringDecisionEngine,
)

from graph_builder.workers.engineering_review_cycle import (
    EngineeringReviewCycle,
)

from graph_builder.workers.engineering_task import (
    EngineeringTask,
)

print("\n========================================")
print("Engineering Decision Engine")
print("========================================\n")

engine = EngineeringDecisionEngine()

cycle = EngineeringReviewCycle()

task = EngineeringTask(

    title="Implement Runtime Scheduler",

    description="Runtime scheduling engine",

    priority="HIGH",

)

task.start()

review = cycle.execute(task)

print("Remember\n")

pprint(

    engine.remember(review)

)

print("\nDecision\n")

pprint(

    engine.decide(

        task.to_dict()

    )

)

print("\nEngine Status\n")

pprint(

    engine.status()

)