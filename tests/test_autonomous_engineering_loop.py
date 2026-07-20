from pprint import pprint

from graph_builder.runtime.autonomous_engineering_loop import (
    AutonomousEngineeringLoop,
)

from graph_builder.workers.worker_registry import (
    WorkerRegistry,
)

from graph_builder.workers.repository_architect_worker import (
    RepositoryArchitectWorker,
)

from graph_builder.workers.code_engineer_worker import (
    CodeEngineerWorker,
)

from graph_builder.workers.testing_engineer_worker import (
    TestingEngineerWorker,
)

print("\n========================================")
print("Autonomous Engineering Loop")
print("========================================\n")

registry = WorkerRegistry()

registry.register(

    RepositoryArchitectWorker()

)

registry.register(

    CodeEngineerWorker()

)

registry.register(

    TestingEngineerWorker()

)

reasoning = {

    "executive_priority":

        "EXPANSION",

    "executive_recommendation":

        "Expand repository engineering capabilities.",

}

loop = AutonomousEngineeringLoop(

    reasoning,

    registry,

)

pprint(

    loop.run()

)