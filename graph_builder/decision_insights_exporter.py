import json

from graph_builder.decision_insights import (
    generate_decision_insights
)


def export_decision_insights(
    output_file
):

    insights = (
        generate_decision_insights()
    )

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            insights,
            file,
            indent=4
        )

    return insights
