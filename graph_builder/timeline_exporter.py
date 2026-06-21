from graph_builder.repository_timeline import (
    generate_repository_timeline
)


def export_repository_timeline(
    output_file
):

    timeline = (
        generate_repository_timeline()
    )

    lines = []

    lines.append(
        "# Repository Timeline"
    )

    lines.append("")

    for item in timeline:

        lines.append(
            f"## {item['stage']}"
        )

        lines.append("")

        lines.append(
            item["title"]
        )

        lines.append("")

        lines.append(
            "Features:"
        )

        for feature in item[
            "features"
        ]:

            lines.append(
                f"- {feature}"
            )

        lines.append("")

        lines.append(
            f"Commit: {item['commit']}"
        )

        lines.append("")

        lines.append(
            "---"
        )

        lines.append("")

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            "\n".join(lines)
        )

    return "\n".join(lines)