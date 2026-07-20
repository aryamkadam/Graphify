from pprint import pprint

from graph_builder.workers.engineering_task import EngineeringTask


def main():

    task = EngineeringTask(

        title="Repository Assessment",

        description="Analyze repository architecture.",

        priority="HIGH",

    )

    task.assign("Repository Architect")

    task.set_complexity("HIGH")

    task.set_expected_output(

        "Architecture Assessment Report"

    )

    task.set_estimated_effort("3 hours")

    task.add_dependency("TASK-0001")

    task.add_tag("architecture")

    task.add_tag("analysis")

    task.start()

    task.complete(

        "Architecture successfully assessed."

    )

    print("\n========================================")
    print("Engineering Task Evolution")
    print("========================================\n")

    pprint(task.to_dict())


if __name__ == "__main__":
    main()