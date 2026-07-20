from pprint import pprint

from graph_builder.workers.engineering_task import EngineeringTask

from graph_builder.workers.repository_architect import RepositoryArchitect

from graph_builder.workers.code_engineer import CodeEngineer

from graph_builder.workers.worker_execution_coordinator import (
    WorkerExecutionCoordinator,
)

from graph_builder.workers.worker_collaboration_engine import (
    WorkerCollaborationEngine,
)


def main():

    task = EngineeringTask(

        title="Repository Assessment",

        description="Improve architecture",

        priority="HIGH",

    )

    coordinator = WorkerExecutionCoordinator()

    collaboration = WorkerCollaborationEngine(

        coordinator,

    )

    workers = [

        RepositoryArchitect(),

        CodeEngineer(),

    ]

    report = collaboration.execute(

        task,

        workers,

    )

    print("\n========================================")

    print("Worker Collaboration Engine")

    print("========================================\n")

    pprint(

        {

            "workers":

                report["workers"],

            "status":

                report["status"],

            "task":

                report["task"].to_dict(),

            "collaboration_log":

                report["collaboration_log"],

            "version":

                report["version"],

        }

    )


if __name__ == "__main__":

    main()