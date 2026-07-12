from pprint import pprint

from graph_builder.runtime.runtime_brain import RuntimeBrain
from graph_builder.executive.executive_feedback_engine import (
    ExecutiveFeedbackEngine,
)

print("\n========================================")
print("Executive Feedback Engine")
print("========================================\n")

brain = RuntimeBrain()

feedback = ExecutiveFeedbackEngine(

    brain.registry,

)

pprint(

    feedback.analyze()

)