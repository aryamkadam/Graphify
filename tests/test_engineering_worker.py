from pprint import pprint

from graph_builder.workers.engineering_worker import EngineeringWorker


def main():

    worker = EngineeringWorker(

        worker_name="Repository Architect",

        role="Architecture",

    )

    print("\n========================================")
    print("Engineering Worker")
    print("========================================\n")

    print("Initial State\n")

    pprint(worker.state())

    worker.assign(

        "Repository Assessment",

    )

    print("\nAfter Assignment\n")

    pprint(worker.state())

    worker.start()

    print("\nDuring Execution\n")

    pprint(worker.state())

    report = worker.complete(

        result="Repository successfully assessed.",

    )

    print("\nCompletion Report\n")

    pprint(report)

    print("\nFinal State\n")

    pprint(worker.state())


if __name__ == "__main__":

    main()