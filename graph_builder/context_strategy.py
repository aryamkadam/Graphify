def generate_strategy(
    context,
    target_health=90
):

    repository = context[
        "repository"
    ]

    current_health = (
        repository[
            "health_score"
        ]
    )

    recommendations = (
        repository[
            "top_recommendations"
        ]
    )

    steps = []

    step_number = 1

    for item in recommendations:

        steps.append({

            "step":
                step_number,

            "action":
                item[
                    "message"
                ],

            "priority":
                item[
                    "priority"
                ]
        })

        step_number += 1

    gap = (
        target_health -
        current_health
    )

    if gap <= 0:

        effort = (
            "Minimal"
        )

    elif gap <= 10:

        effort = (
            "Low"
        )

    elif gap <= 20:

        effort = (
            "Medium"
        )

    else:

        effort = (
            "High"
        )

    return {

        "current_health":
            current_health,

        "target_health":
            target_health,

        "estimated_effort":
            effort,

        "strategy_steps":
            steps
    }