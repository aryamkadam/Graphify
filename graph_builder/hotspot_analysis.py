from graph_builder.query_engine import (
    load_symbol_index
)


def detect_hotspots(
    symbol_index
):

    file_stats = {}

    for symbol, data in symbol_index.items():

        file_name = data["file"]

        usage_count = sum(
            usage["count"]
            for usage in data["used_by"]
        )

        if file_name not in file_stats:

            file_stats[file_name] = {
                "file": file_name,
                "symbols": 0,
                "usage_count": 0
            }

        file_stats[file_name][
            "symbols"
        ] += 1

        file_stats[file_name][
            "usage_count"
        ] += usage_count

    hotspots = list(
        file_stats.values()
    )

    hotspots.sort(
        key=lambda x: x["usage_count"],
        reverse=True
    )

    return hotspots