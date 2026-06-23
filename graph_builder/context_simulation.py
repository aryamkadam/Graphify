def simulate_change(
    context,
    target_symbol
):

    repository = context[
        "repository"
    ]

    critical_symbols = (
        repository[
            "critical_symbols"
        ]
    )

    risky_symbols = (
        repository[
            "risky_symbols"
        ]
    )

    risk_level = "LOW"

    affected_count = 3

    recommendation = (
        "Safe to modify."
    )

    if target_symbol in critical_symbols:

        risk_level = "HIGH"

        affected_count = 20

        recommendation = (
            "Refactor gradually."
        )

    elif target_symbol in risky_symbols:

        risk_level = "MEDIUM"

        affected_count = 10

        recommendation = (
            "Perform impact testing."
        )

    return {

        "symbol":
            target_symbol,

        "risk_level":
            risk_level,

        "affected_symbols":
            affected_count,

        "recommendation":
            recommendation
    }