from graph_builder.context_replay import (
    generate_context_replay
)


def export_context_replay():

    replay = (
        generate_context_replay()
    )

    lines = []

    lines.append(
        "# Context Replay Timeline"
    )

    lines.append("")

    for item in replay:

        lines.append(

            f"Version "
            f"{item['version']}"

        )

        lines.append(

            f"Stage: "
            f"{item['stage']}"

        )

        lines.append(

            f"Health: "
            f"{item['health_score']}"

        )

        lines.append(

            f"Message: "
            f"{item['message']}"

        )

        lines.append("")

    return "\n".join(
        lines
    )