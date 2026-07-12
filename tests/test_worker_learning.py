from pprint import pprint

from graph_builder.workers.worker_learning import (
    WorkerLearning,
)

print("\n========================================")
print("Worker Learning Engine")
print("========================================\n")

learning = WorkerLearning()

learning.learn(
    "Plugin architecture reduces coupling."
)

learning.learn(
    "Avoid circular dependencies."
)

learning.learn(
    "Runtime scheduler should remain modular.",
    score=20,
)

print("Profile\n")

pprint(
    learning.profile()
)

print("\nHistory\n")

pprint(
    learning.history()
)