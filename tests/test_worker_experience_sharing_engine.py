from pprint import pprint

from graph_builder.workers.engineering_task import EngineeringTask

from graph_builder.workers.worker_memory_engine import (
    WorkerMemoryEngine,
)

from graph_builder.workers.worker_experience_sharing_engine import (
    WorkerExperienceSharingEngine,
)


def main():

    architect = WorkerMemoryEngine(

        "Repository Architect",

    )

    engineer = WorkerMemoryEngine(

        "Code Engineer",

    )

    task = EngineeringTask(

        title="Repository Assessment",

        priority="HIGH",

    )

    task.complete(

        "Architecture successfully assessed.",

    )

    architect.remember(

        task,

    )

    sharing = WorkerExperienceSharingEngine()

    report = sharing.share(

        architect,

        engineer,

    )

    print("\n========================================")
    print("Worker Experience Sharing Engine")
    print("========================================\n")

    print("Sharing Report\n")

    pprint(report)

    print("\nEngineer Memory\n")

    pprint(engineer.history())

    print("\nEngineer Summary\n")

    pprint(engineer.summary())


if __name__ == "__main__":
    main()