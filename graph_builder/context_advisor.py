def generate_context_advice(
    context
):

    recommendations = (
        context[
            "repository"
        ][
            "top_recommendations"
        ]
    )

    if len(
        recommendations
    ) == 0:

        return {

            "next_action":
                "No action required",

            "priority":
                "NONE",

            "expected_gain":
                0,

            "reason":
                "Repository is healthy"
        }

    best = max(
        recommendations,
        key=lambda item:
        item["score"]
    )

    score = best[
        "score"
    ]

    expected_gain = min(
        10,
        max(
            1,
            score // 20
        )
    )

    return {

        "next_action":
            best[
                "message"
            ],

        "priority":
            best[
                "priority"
            ],

        "expected_gain":
            expected_gain,

        "reason":
            "Highest impact recommendation"
    }