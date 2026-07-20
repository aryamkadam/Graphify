from pprint import pprint

from graph_builder.runtime.engineering_cycle import EngineeringCycle
from graph_builder.runtime.runtime_session import RuntimeSession


def main():

    session = RuntimeSession()

    cycle = EngineeringCycle(

        strategy="Continuous Quality Expansion",

    )

    cycle.start()

    session.begin(

        cycle,

    )

    print("\n========================================")
    print("Runtime Session")
    print("========================================\n")

    print("Running Session\n")

    pprint(session.summary())

    cycle.complete()

    session.complete()

    print("\nCompleted Session\n")

    pprint(session.summary())


if __name__ == "__main__":
    main()