def generate_architecture_summary(
    symbol_index
):

    layers = {}

    for symbol, data in symbol_index.items():

        file_path = data["file"]

        folder = (
            file_path.split("\\")[0]
        )

        if folder not in layers:

            layers[folder] = []

        layers[folder].append(
            file_path
        )

    lines = []

    lines.append(
        "# Architecture Summary"
    )

    lines.append("")

    for layer in sorted(
        layers.keys()
    ):

        lines.append(
            f"## {layer}"
        )

        unique_files = sorted(
            set(
                layers[layer]
            )
        )

        for file_name in unique_files:

            lines.append(
                f"- {file_name}"
            )

        lines.append("")

    return "\n".join(
        lines
    )