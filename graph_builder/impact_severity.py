from graph_builder.impact_predictor import (
    predict_impact
)


def calculate_impact_severity(
    symbol,
    knowledge_graph
):

    impacted = predict_impact(
        symbol,
        knowledge_graph
    )

    score = len(
        set(impacted)
    )

    if score >= 5:

        severity = "HIGH"

    elif score >= 2:

        severity = "MEDIUM"

    else:

        severity = "LOW"

    return {
        "symbol": symbol,
        "impact_score": score,
        "severity": severity
    }