from graph_builder.decision_categories import (
    generate_decision_categories
)


def generate_decision_trends(
    decisions
):

    categories = (
        generate_decision_categories(
            decisions
        )
    )

    dominant_area = max(
        categories,
        key=categories.get
    )

    return {

        "dominant_area":
            dominant_area,

        "category_counts":
            categories
    }