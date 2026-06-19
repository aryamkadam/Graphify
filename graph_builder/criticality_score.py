from graph_builder.dependency_depth import (
    calculate_depth
)


def calculate_criticality(
    symbol_index
):

    results = []

    for symbol, info in symbol_index.items():

        usage_count = sum(
            usage["count"]
            for usage in info["used_by"]
        )

        depth = calculate_depth(
            symbol,
            symbol_index
        )

        score = (
            usage_count * 2
        ) + depth

        results.append(
            {
                "symbol": symbol,
                "score": score,
                "usage_count": usage_count,
                "depth": depth,
                "file": info["file"]
            }
        )

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return results