from graph_builder.decision_history import (
    build_decision_history
)


def generate_decision_reasoning_pack():

    decisions = (
        build_decision_history()
    )

    lines = []

    lines.append(
        "# Decision Reasoning Pack"
    )

    lines.append("")

    for decision in decisions:

        lines.append(
            f"## {decision['title']}"
        )

        lines.append("")

        lines.append(
            f"Reason: "
            f"{decision['reason']}"
        )

        lines.append("")

        lines.append(
            f"Impact: "
            f"{decision['impact']}"
        )

        lines.append("")

        lines.append(
            f"Stage: "
            f"{decision['stage']}"
        )

        if decision["commit"]:

            lines.append("")

            lines.append(
                f"Commit: "
                f"{decision['commit']}"
            )

        lines.append("")
        lines.append("---")
        lines.append("")

    return "\n".join(
        lines
    )