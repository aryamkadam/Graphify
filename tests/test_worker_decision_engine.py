from pprint import pprint

from graph_builder.workers.worker_identity import (
    WorkerIdentity,
)

from graph_builder.workers.worker_memory import (
    WorkerMemory,
)

from graph_builder.workers.worker_goals import (
    WorkerGoals,
)

from graph_builder.workers.worker_learning import (
    WorkerLearning,
)

from graph_builder.workers.worker_experience import (
    WorkerExperience,
)

from graph_builder.workers.worker_decision_engine import (
    WorkerDecisionEngine,
)

print("\n========================================")
print("Worker Decision Engine")
print("========================================\n")

identity = WorkerIdentity(

    "Repository Architect",

    "Architecture",

)

memory = WorkerMemory()

memory.remember(

    "Architecture",

    "Prefer plugin architecture.",

)

goals = WorkerGoals()

goals.set_current_goal(

    "Reduce Repository Coupling",

)

learning = WorkerLearning()

learning.learn(

    "Plugin architecture scales well.",

    20,

)

experience = WorkerExperience()

for _ in range(35):

    experience.gain(

        10,

    )

engine = WorkerDecisionEngine(

    identity,

    memory,

    goals,

    learning,

    experience,

)

pprint(

    engine.decide(

        "Refactor Authentication"

    )

)