from pprint import pprint

from graph_builder.executive.executive_scheduler import (
    ExecutiveScheduler,
)

from graph_builder.executive.worker_selection_engine import (
    WorkerSelectionEngine,
)

from graph_builder.executive.dispatch_pipeline import (
    DispatchPipeline,
)

from graph_builder.workers.worker_registry import (
    WorkerRegistry,
)

print("\n========================================")
print("Dispatch Pipeline")
print("========================================\n")

registry = WorkerRegistry()
registry.register_default_workers()

scheduler = ExecutiveScheduler()

selector = WorkerSelectionEngine(
    registry
)

pipeline = DispatchPipeline(
    scheduler,
    selector,
)

print("Pipeline Status\n")

pprint(
    pipeline.status()
)

print("\nArchitecture Task\n")

pprint(
    pipeline.execute(
        "Improve Repository Architecture",
        "architecture",
    )
)

print("\nImplementation Task\n")

pprint(
    pipeline.execute(
        "Implement Runtime Scheduler",
        "implementation",
    )
)

print("\nTesting Task\n")

pprint(
    pipeline.execute(
        "Verify Runtime Scheduler",
        "testing",
    )
)

print("\nUnknown Task\n")

pprint(
    pipeline.execute(
        "Deploy Infrastructure",
        "deployment",
    )
)