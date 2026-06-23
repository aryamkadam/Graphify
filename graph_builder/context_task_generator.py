def generate_tasks(
    context
):

    recommendations = (
        context[
            "repository"
        ][
            "top_recommendations"
        ]
    )

    tasks = []

    task_id = 1

    for item in recommendations:

        tasks.append(

            {
                "task_id":
                    task_id,

                "type":
                    "Repository Improvement",

                "target":
                    item[
                        "message"
                    ],

                "priority":
                    item[
                        "priority"
                    ],

                "estimated_gain":
                    max(
                        1,
                        item[
                            "score"
                        ] // 20
                    )
            }
        )

        task_id += 1

    return tasks