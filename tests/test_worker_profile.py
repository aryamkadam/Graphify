from pprint import pprint

from graph_builder.workers.worker_profile import WorkerProfile

print("\n========================================")
print("Worker Profile")
print("========================================\n")

profile = WorkerProfile(

    "Repository Architect",

    "Architecture",

)

print("Status\n")

pprint(

    profile.status()

)

print("\nIdentity\n")

pprint(

    profile.identity.profile()

)