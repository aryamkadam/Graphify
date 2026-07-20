from pprint import pprint

from graph_builder.runtime.autonomous_runtime_scheduler import (
    AutonomousRuntimeScheduler,
)


def main():

    scheduler = AutonomousRuntimeScheduler()

    repository_event = {

        "requires_engineering": True,

        "reason": "Repository structure changed.",

    }

    print("\n========================================")
    print("Autonomous Runtime Scheduler")
    print("========================================\n")

    result = scheduler.evaluate(

        repository_event,

    )

    pprint(result)


if __name__ == "__main__":

    main()