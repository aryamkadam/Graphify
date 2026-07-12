from pprint import pprint

from graph_builder.workers.worker_registry import WorkerRegistry

print("\n========================================")
print("Worker Boot Engine")
print("========================================\n")

registry = WorkerRegistry()

registry.register_default_workers()

print("Registry Status\n")

pprint(

    registry.status()

)

print("\nWorkers\n")

pprint(

    registry.all_workers()

)