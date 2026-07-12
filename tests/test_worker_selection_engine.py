from pprint import pprint

from graph_builder.workers.worker_registry import (
    WorkerRegistry,
)

from graph_builder.executive.worker_selection_engine import (
    WorkerSelectionEngine,
)

print("\n========================================")
print("Worker Selection Engine")
print("========================================\n")

registry = WorkerRegistry()

registry.register_default_workers()

engine = WorkerSelectionEngine(registry)

print("Status\n")

pprint(engine.status())

print("\nArchitecture Task\n")

pprint(engine.select("architecture"))

print("\nImplementation Task\n")

pprint(engine.select("implementation"))

print("\nTesting Task\n")

pprint(engine.select("testing"))

print("\nUnknown Task\n")

pprint(engine.select("deployment"))