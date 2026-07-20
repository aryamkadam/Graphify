from pprint import pprint

from graph_builder.workers.engineering_task import EngineeringTask

from graph_builder.workers.worker_memory_engine import (

    WorkerMemoryEngine,

)


def main():

    memory = WorkerMemoryEngine(

        "Repository Architect",

    )

    task = EngineeringTask(

        title="Repository Assessment",

        priority="HIGH",

    )

    task.complete(

        "Architecture successfully assessed.",

    )

    memory.remember(

        task,

    )

    print("\n========================================")

    print("Worker Memory Engine")

    print("========================================\n")

    pprint(memory.history())

    print("\nSummary\n")

    pprint(memory.summary())


if __name__ == "__main__":

    main()