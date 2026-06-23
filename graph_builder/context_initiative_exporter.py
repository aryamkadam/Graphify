from graph_builder.context_initiative_engine import (
    generate_initiatives
)


def export_initiatives(
    context
):

    initiatives = (
        generate_initiatives(
            context
        )
    )

    lines = []

    lines.append(
        "# Context Initiatives"
    )

    lines.append("")

    for item in initiatives:

        lines.append(
            item[
                "initiative"
            ]
        )

        lines.append(
            "-" * 30
        )

        lines.append(

            f"Tasks: "
            f"{item['task_count']}"

        )

        lines.append(

            f"Expected Gain: "
            f"{item['expected_gain']}"

        )

        lines.append("")

    return "\n".join(
        lines
    )