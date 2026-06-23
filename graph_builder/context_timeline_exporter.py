from graph_builder.context_timeline import (
    generate_context_timeline
)


def export_context_timeline():

    timeline = (
        generate_context_timeline()
    )

    lines = []

    lines.append(
        "# Context Timeline"
    )

    lines.append("")

    for item in timeline:

        lines.append(
            f"Version {item['version']}"
        )

        lines.append(
            f"Stage: {item['stage']}"
        )

        lines.append(
            f"Health: {item['health_score']}"
        )

        lines.append(
            f"Message: {item['message']}"
        )

        lines.append("")

    return "\n".join(
        lines
    )