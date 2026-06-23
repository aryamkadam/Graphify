from graph_builder.context_task_generator import (
    generate_tasks
)


def generate_execution_plan(
    context
):

    tasks = (
        generate_tasks(
            context
        )
    )

    priority_order = {

        "HIGH": 1,
        "MEDIUM": 2,
        "LOW": 3
    }

    ordered_tasks = sorted(

        tasks,

        key=lambda task:
        (
            priority_order[
                task[
                    "priority"
                ]
            ],
            -task[
                "estimated_gain"
            ]
        )
    )

    plan = []

    step = 1

    for task in ordered_tasks:

        plan.append(

            {
                "step":
                    step,

                "action":
                    task[
                        "target"
                    ],

                "priority":
                    task[
                        "priority"
                    ],

                "expected_gain":
                    task[
                        "estimated_gain"
                    ]
            }
        )

        step += 1

    return plan