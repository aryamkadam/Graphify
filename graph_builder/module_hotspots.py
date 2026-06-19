def detect_module_hotspots(
    hotspot_data
):

    modules = {}

    for item in hotspot_data:

        file_path = item["file"]

        module = file_path.split(
            "\\"
        )[0]

        if module not in modules:

            modules[module] = {
                "module": module,
                "usage_count": 0,
                "files": 0
            }

        modules[module][
            "usage_count"
        ] += item["usage_count"]

        modules[module][
            "files"
        ] += 1

    result = list(
        modules.values()
    )

    result.sort(
        key=lambda x: x["usage_count"],
        reverse=True
    )

    return result