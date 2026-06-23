def generate_forecast(
    context
):

    repository = context[
        "repository"
    ]

    current_health = (
        repository[
            "health_score"
        ]
    )

    dead_code_count = (
        repository[
            "dead_code_count"
        ]
    )

    hotspot_count = (
        repository[
            "hotspot_count"
        ]
    )

    after_dead_code = (
        current_health +
        min(dead_code_count // 2, 5)
    )

    after_refactor = (
        after_dead_code + 8
    )

    after_hotspot_fix = (
        after_refactor +
        min(hotspot_count // 2, 8)
    )

    predicted_final = min(
        after_hotspot_fix,
        100
    )

    return {

        "current_health":
            current_health,

        "after_dead_code_removal":
            after_dead_code,

        "after_refactoring":
            after_refactor,

        "after_hotspot_reduction":
            after_hotspot_fix,

        "predicted_final_health":
            predicted_final
    }