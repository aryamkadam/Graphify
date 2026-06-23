from graph_builder.context_task_generator import (
    generate_tasks
)


def generate_initiatives(
    context
):

    tasks = generate_tasks(
        context
    )

    initiatives = {

        "Parser Refactoring": [],
        "Architecture Cleanup": [],
        "Code Quality": []
    }

    for task in tasks:

        target = task[
            "target"
        ].lower()

        if (
            "parse_python_file" in target
            or
            "extract_parameters" in target
        ):

            initiatives[
                "Parser Refactoring"
            ].append(
                task
            )

        elif (
            "split" in target
            or
            "architecture" in target
        ):

            initiatives[
                "Architecture Cleanup"
            ].append(
                task
            )

        else:

            initiatives[
                "Code Quality"
            ].append(
                task
            )

    result = []

    for name, items in initiatives.items():

        if len(items) == 0:
            continue

        total_gain = sum(
            item[
                "estimated_gain"
            ]
            for item in items
        )

        result.append(

            {
                "initiative":
                    name,

                "task_count":
                    len(items),

                "expected_gain":
                    total_gain,

                "tasks":
                    items
            }
        )

    return result