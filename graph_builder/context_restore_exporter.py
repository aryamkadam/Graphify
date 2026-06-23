def export_restored_context(
    restored
):

    lines = []

    lines.append(
        "# Restored Context"
    )

    lines.append("")

    for key, value in restored.items():

        lines.append(
            f"{key}: {value}"
        )

    return "\n".join(
        lines
    )