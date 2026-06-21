from graph_builder.decision_memory import (
    generate_decision_memory
)


def export_decision_memory(
    output_file
):

    decisions = (
        generate_decision_memory()
    )

    lines = []

    lines.append(
        "# Decision Memory"
    )

    lines.append("")

    for index, item in enumerate(
        decisions,
        start=1
    ):

        lines.append(
            f"## Decision {index}"
        )

        lines.append("")

        lines.append(
            f"Decision:\n{item['decision']}"
        )

        lines.append("")

        lines.append(
            f"Reason:\n{item['reason']}"
        )

        lines.append("")

        lines.append(
            f"Impact:\n{item['impact']}"
        )

        lines.append("")

        lines.append(
            "---"
        )

        lines.append("")

    content = "\n".join(
        lines
    )

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            content
        )

    return content