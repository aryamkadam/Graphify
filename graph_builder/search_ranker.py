def rank_search_results(
    results,
    symbol_index
):

    ranked = []

    for result in results:

        symbol = result["symbol"]

        usage_count = sum(
            usage["count"]
            for usage in symbol_index[
                symbol
            ]["used_by"]
        )

        final_score = (
            result["score"] +
            usage_count
        )

        ranked.append(
            {
                **result,
                "usage_count": usage_count,
                "final_score": final_score
            }
        )

    ranked.sort(
        key=lambda x: x["final_score"],
        reverse=True
    )

    return ranked