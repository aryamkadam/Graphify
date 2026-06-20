from graph_builder.impact_severity import (
    calculate_impact_severity
)


def rank_repository_risks(
    symbol_index,
    knowledge_graph
):

    rankings = []

    for symbol in symbol_index:

        result = calculate_impact_severity(
            symbol,
            knowledge_graph
        )

        rankings.append(
            result
        )

    rankings.sort(
        key=lambda x: x["impact_score"],
        reverse=True
    )

    return rankings