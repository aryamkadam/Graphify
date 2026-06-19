from graph_builder.query_engine import (
    load_symbol_index
)


def detect_critical_symbols(
    symbol_index,
    min_usage=1
):

    critical = []

    for symbol, data in symbol_index.items():

        usage_count = sum(
            usage["count"]
            for usage in data["used_by"]
        )

        if usage_count >= min_usage:

            critical.append(
                {
                    "symbol": symbol,
                    "usage_count": usage_count,
                    "file": data["file"]
                }
            )

    critical.sort(
        key=lambda x: x["usage_count"],
        reverse=True
    )

    return critical