from graph_builder.dependency_depth import (
    calculate_depth
)

from graph_builder.impact_predictor import (
    predict_impact
)


def rank_critical_symbols(
    symbol_index,
    knowledge_graph
):

    rankings = []

    for symbol, data in symbol_index.items():

        usage_count = sum(
            usage["count"]
            for usage in data["used_by"]
        )

        depth = calculate_depth(
            symbol,
            symbol_index
        )

        impact_score = len(
            set(
                predict_impact(
                    symbol,
                    knowledge_graph
                )
            )
        )

        critical_score = (
            usage_count +
            depth +
            impact_score
        )

        rankings.append(
            {
                "symbol": symbol,
                "critical_score": critical_score,
                "usage_count": usage_count,
                "depth": depth,
                "impact_score": impact_score,
                "file": data["file"]
            }
        )

    rankings.sort(
        key=lambda x: x["critical_score"],
        reverse=True
    )

    return rankings