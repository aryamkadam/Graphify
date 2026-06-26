def generate_strategy(
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

    actions = (
        continuation.get(
            "recommended_actions",
            []
        )
    )

    steps = []

    step_number = 1

    for action in actions:

        steps.append({

            "step":
                step_number,

            "action":
                action,

            "priority":
                "HIGH"
        })

        step_number += 1

    gap = (
        target_transfer_score -
        current_score
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

        "current_transfer_score":
            current_score,

        "target_transfer_score":
            target_transfer_score,

        "estimated_effort":
            effort,

        "strategy_steps":
            steps
    }