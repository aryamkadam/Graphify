def generate_context_advice(
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

    if len(actions) == 0:

        return {

            "next_action":
                "No action required",

            "priority":
                "NONE",

            "expected_gain":
                0,

            "reason":
                "Context transfer capability is already complete"
        }

    next_action = actions[0]

    expected_gain = min(
        10,
        max(
            1,
            (100 - transfer_score) // 10
        )
    )

    return {

        "next_action":
            next_action,

        "priority":
            "HIGH",

        "expected_gain":
            expected_gain,

        "reason":
            "Highest impact action for improving AI context transfer"
    }