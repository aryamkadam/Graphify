def detect_god_files(
    symbol_index,
    threshold=3
):

    files = {}

    for symbol, data in symbol_index.items():

        file = data["file"]

        if file not in files:

            files[file] = {
                "symbols": 0,
                "usage_count": 0
            }

        files[file]["symbols"] += 1

        files[file]["usage_count"] += sum(
            usage["count"]
            for usage in data["used_by"]
        )

    results = []

    for file, stats in files.items():

        if stats["symbols"] >= threshold:

            results.append(
                {
                    "file": file,
                    "symbols": stats["symbols"],
                    "usage_count":
                    stats["usage_count"]
                }
            )

    results.sort(
        key=lambda x: (
            x["symbols"],
            x["usage_count"]
        ),
        reverse=True
    )

    return results