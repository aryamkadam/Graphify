from graph_builder.repository_brain import (
    generate_repository_brain
)


def generate_context_intelligence(
    repository_brain
):

    health_score = repository_brain[
        "health_score"
    ]

    direction = repository_brain[
        "project_direction"
    ]

    if health_score >= 90:
        maturity = "PRODUCTION_READY"

    elif health_score >= 70:
        maturity = "ADVANCED"

    elif health_score >= 50:
        maturity = "INTERMEDIATE"

    else:
        maturity = "BEGINNER"

    if health_score >= 70:
        risk_trend = "DECREASING"
    else:
        risk_trend = "INCREASING"

    ai_readiness = min(
        100,
        health_score + 20
    )

    if direction == "architecture":

        future_direction = (
            "AI Memory Infrastructure"
        )

    elif direction == "memory":

        future_direction = (
            "Persistent AI Memory"
        )

    else:

        future_direction = (
            "Platform Expansion"
        )

    intelligence = {

        "project_maturity":
            maturity,

        "development_pattern":
            direction.upper(),

        "risk_trend":
            risk_trend,

        "ai_readiness":
            ai_readiness,

        "predicted_direction":
            future_direction
    }

    return intelligence