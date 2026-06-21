from graph_builder.decision_history import (
    build_decision_history
)

from graph_builder.decision_trends import (
    generate_decision_trends
)


def generate_decision_insights():

    decisions = (
        build_decision_history()
    )

    trends = (
        generate_decision_trends(
            decisions
        )
    )

    insights = {

        "decision_count":
            len(decisions),

        "dominant_area":
            trends[
                "dominant_area"
            ],

        "category_counts":
            trends[
                "category_counts"
            ]
    }

    return insights