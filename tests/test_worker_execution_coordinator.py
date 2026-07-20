from pprint import pprint

from graph_builder.workers.engineering_task import EngineeringTask
from graph_builder.workers.repository_architect import RepositoryArchitect
from graph_builder.workers.worker_execution_coordinator import (
    WorkerExecutionCoordinator,
)


def main():

    task = EngineeringTask(

        title="Repository Assessment",

        description="Analyze repository architecture.",

        priority="HIGH",

    )

    worker = RepositoryArchitect()

    coordinator = WorkerExecutionCoordinator()

    completed = coordinator.execute(

        task,

        worker,

    )

    print("\n========================================")
    print("Worker Execution Coordinator")
    print("========================================\n")

    pprint(completed.to_dict())

    print("\nWorker State\n")

    pprint(worker.state())


if __name__ == "__main__":

    main()