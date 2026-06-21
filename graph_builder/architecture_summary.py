def generate_architecture_summary(
    symbol_index
):

    layers = {}

    layer_descriptions = {
        "cli":
        "Entry point of Graphify. Handles user execution and startup.",

        "scanner":
        "Discovers repository files and performs file analysis.",

        "parser":
        "Extracts symbols, classes, functions and imports from source code.",

        "graph_builder":
        "Builds repository intelligence including knowledge graphs, dependency analysis, risk analysis, repository brain and AI handover packs."
    }

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

    lines.append(
        "## Repository Flow"
    )

    lines.append("")

    lines.append("Repository")
    lines.append("↓")
    lines.append("Scanner Layer")
    lines.append("↓")
    lines.append("Parser Layer")
    lines.append("↓")
    lines.append("Symbol Index")
    lines.append("↓")
    lines.append("Knowledge Graph")
    lines.append("↓")
    lines.append("Risk Engine")
    lines.append("↓")
    lines.append("Repository Brain")
    lines.append("↓")
    lines.append("AI Handover Pack")

    lines.append("")

    for layer in sorted(
        layers.keys()
    ):

        lines.append(
            f"## {layer.upper()} Layer"
        )

        lines.append("")

        description = (
            layer_descriptions.get(
                layer,
                "Repository component."
            )
        )

        lines.append(
            f"Purpose: {description}"
        )

        lines.append("")

        lines.append(
            "Files:"
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