from graph_builder.repository_health_report import (
    generate_health_report
)


def calculate_project_risk(
    symbol_index,
    knowledge_graph
):

    report = (
        generate_health_report(
            symbol_index,
            knowledge_graph
        )
    )

    risk_score = 100 - report[
        "health_score"
    ]

    if risk_score <= 25:

        level = "LOW"

    elif risk_score <= 50:

        level = "MEDIUM"

    else:

        level = "HIGH"

    return {

        "risk_score":
            risk_score,

        "risk_level":
            level
    }