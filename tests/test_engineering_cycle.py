from pprint import pprint

from graph_builder.runtime.engineering_cycle import EngineeringCycle


def main():

    cycle = EngineeringCycle(

        strategy="Continuous Quality Expansion",

    )

    cycle.start()

    cycle.add_task(

        "Repository Assessment",

    )

    cycle.add_task(

        "Architecture Review",

    )

    cycle.add_result(

        "Repository architecture improved.",

    )

    cycle.add_lesson(

        "Architectural reviews reduce future technical debt.",

    )

    cycle.complete()

    print("\n========================================")
    print("Engineering Cycle")
    print("========================================\n")

    pprint(cycle.summary())


if __name__ == "__main__":
    main()