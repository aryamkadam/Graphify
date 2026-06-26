from graph_builder.context_forecast import (
    generate_forecast
)


def generate_goal_plan(
    context,
    target_transfer_score=100
):

    quality = context.get(
        "quality",
        {}
    )

    continuation = context.get(
        "continuation",
        {}
    )

    current_score = (
        quality.get(
            "transfer_score",
            0
        )
    )

    forecast = (
        generate_forecast(
            context
        )
    )

    predicted = (
        forecast[
            "predicted_final_score"
        ]
    )

    gap = (
        target_transfer_score -
        current_score
    )

    actions = []

    if current_score < target_transfer_score:

        actions.extend(
            continuation.get(
                "recommended_actions",
                []
            )
        )

    probability = max(
        50,
        min(
            100,
            int(
                (predicted /
                 target_transfer_score)
                * 100
            )
        )
    )

    return {

        "current_transfer_score":
            current_score,

        "target_transfer_score":
            target_transfer_score,

        "score_gap":
            gap,

        "predicted_score":
            predicted,

        "success_probability":
            probability,

        "required_actions":
            actions
    }