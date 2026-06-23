from graph_builder.context_forecast import (
    generate_forecast
)


def generate_goal_plan(
    context,
    target_health=95
):

    repository = context[
        "repository"
    ]

    current_health = (
        repository[
            "health_score"
        ]
    )

    forecast = (
        generate_forecast(
            context
        )
    )

    predicted = (
        forecast[
            "predicted_final_health"
        ]
    )

    gap = (
        target_health -
        current_health
    )

    actions = []

    if current_health < target_health:

        actions.append(
            "Remove dead symbols"
        )

        actions.append(
            "Refactor critical symbols"
        )

        actions.append(
            "Reduce repository hotspots"
        )

        actions.append(
            "Improve module structure"
        )

    probability = max(
        50,
        min(
            100,
            int(
                (predicted / target_health)
                * 100
            )
        )
    )

    return {

        "current_health":
            current_health,

        "target_health":
            target_health,

        "health_gap":
            gap,

        "predicted_health":
            predicted,

        "success_probability":
            probability,

        "required_actions":
            actions
    }