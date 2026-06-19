def detect_single_points_of_failure(
    symbol_index,
    threshold=3
):

    risks = []

    for symbol, data in symbol_index.items():

        usage_count = sum(
            usage["count"]
            for usage in data["used_by"]
        )

        if usage_count >= threshold:

            risks.append(
                {
                    "risk":
                    "single_point_of_failure",

                    "symbol":
                    symbol,

                    "usage_count":
                    usage_count,

                    "file":
                    data["file"]
                }
            )

    risks.sort(
        key=lambda x:
        x["usage_count"],
        reverse=True
    )

    return risks