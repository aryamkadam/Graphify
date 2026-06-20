from graph_builder.dependency_depth import (
    calculate_depth
)

from graph_builder.impact_predictor import (
    predict_impact
)


def generate_symbol_context(
    symbol,
    symbol_index,
    knowledge_graph
):

    data = symbol_index.get(
        symbol
    )

    if not data:
        return None

    usage_count = sum(
        usage["count"]
        for usage in data["used_by"]
    )

    dependency_depth = calculate_depth(
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
        usage_count
        +
        dependency_depth
        +
        impact_score
    )

    return {
        "symbol": symbol,
        "file": data["file"],
        "type": data["type"],
        "line": data["line"],
        "parameters": data.get(
            "parameters",
            []
        ),
        "usage_count": usage_count,
        "dependency_depth": dependency_depth,
        "impact_score": impact_score,
        "critical_score": critical_score
    }