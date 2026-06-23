from graph_builder.context_roadmap import (
    generate_roadmap
)


def export_roadmap(
    context,
    target_health=95
):

    roadmap = generate_roadmap(
        context,
        target_health
    )

    lines = []

    lines.append(
        "# Context Roadmap"
    )

    lines.append("")

    lines.append(
        f"Current Health: "
        f"{roadmap['current_health']}"
    )

    lines.append(
        f"Target Health: "
        f"{roadmap['target_health']}"
    )

    lines.append(
        f"Confidence: "
        f"{roadmap['confidence']}%"
    )

    lines.append(
        f"Estimated Duration: "
        f"{roadmap['estimated_duration']}"
    )

    lines.append("")

    for phase in roadmap[
        "phases"
    ]:

        lines.append(
            f"Phase {phase['phase']}"
        )

        lines.append(
            phase["title"]
        )

        lines.append(
            f"Expected Health: "
            f"{phase['expected_health']}"
        )

        lines.append("")

    return "\n".join(
        lines
    )