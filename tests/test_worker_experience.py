from pprint import pprint

from graph_builder.workers.worker_experience import (
    WorkerExperience,
)

print("\n========================================")
print("Worker Experience Engine")
print("========================================\n")

experience = WorkerExperience()

for _ in range(25):

    experience.gain(10)

print("Profile\n")

pprint(

    experience.profile()

)

for _ in range(80):

    experience.gain(10)

print("\nAfter Long Experience\n")

pprint(

    experience.profile()

)