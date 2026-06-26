def generate_tasks(
    context
):

    continuation = context.get(
        "continuation",
        {}
    )

    quality = context.get(
        "quality",
        {}
    )

    actions = continuation.get(
        "recommended_actions",
        []
    )

    transfer_score = quality.get(
        "transfer_score",
        0
    )

    tasks = []

    task_id = 1

    estimated_gain = max(
        1,
        (100 - transfer_score) // 10
    )

    for action in actions:

        tasks.append(

            {

                "task_id":
                    task_id,

                "type":
                    "AI Context Transfer",

                "target":
                    action,

                "priority":
                    "HIGH",

                "estimated_gain":
                    estimated_gain
            }

        )

        task_id += 1

    return tasks