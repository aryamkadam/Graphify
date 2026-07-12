from pprint import pprint

from graph_builder.workers.worker_goals import (
    WorkerGoals,
)

print("\n========================================")
print("Worker Goals Engine")
print("========================================\n")

goals = WorkerGoals()

goals.set_current_goal(

    "Reduce Repository Coupling"

)

goals.set_long_term_goal(

    "Create Self-Evolving Repository"

)

goals.update_progress(25)

goals.update_progress(40)

print("Profile\n")

pprint(

    goals.profile()

)

goals.update_progress(35)

print("\nCompleted\n")

pprint(

    goals.profile()

)