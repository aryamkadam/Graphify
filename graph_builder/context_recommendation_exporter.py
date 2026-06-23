from graph_builder.context_recommendation import (
    generate_context_recommendations
)


def export_recommendation_report(
    context
):

    report = (
        generate_context_recommendations(
            context
        )
    )

    lines = []

    lines.append(
        "# Context Recommendation Report"
    )

    lines.append("")

    lines.append(
        f"Health Score: "
        f"{report['health_score']}"
    )

    lines.append("")

    for item in report[
        "recommendations"
    ]:

        lines.append(
            f"[{item['priority']}] "
            f"{item['message']}"
        )

    return "\n".join(
        lines
    )