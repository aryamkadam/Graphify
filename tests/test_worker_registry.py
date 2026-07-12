from pprint import pprint

from graph_builder.workers.base_worker import BaseWorker
from graph_builder.workers.worker_registry import WorkerRegistry

print("\n========================================")
print("Worker Registry")
print("========================================\n")

registry = WorkerRegistry()

architect = BaseWorker("Repository Architect")
tester = BaseWorker("Testing Engineer")
engineer = BaseWorker("Code Engineer")

registry.register(architect)
registry.register(tester)
registry.register(engineer)

print("Status\n")
pprint(registry.status())

print("\nAll Workers\n")
pprint(registry.all_workers())

print("\nRetrieve Worker\n")
worker = registry.get("Repository Architect")
pprint(worker.report())

print("\nExists\n")
print(registry.exists("Testing Engineer"))

print("\nMissing\n")
print(registry.get("Planner"))