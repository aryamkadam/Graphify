from graph_builder.decision_replay import (
    generate_decision_replay
)

from graph_builder.context_history import (
    get_context_history
)


def generate_session_reconstruction():

    history = (
        get_context_history()
    )

    decisions = (
        generate_decision_replay()
    )

    lines = []

    lines.append(
        "=== GRAPHIFY SESSION RECONSTRUCTION ==="
    )

    lines.append("")

    lines.append(
        "Project Evolution:"
    )

    for item in history:

        lines.append(

            f"- {item.get('message','')}"
        )

    lines.append("")

    lines.append(
        "Decision Narrative:"
    )

    for decision in decisions:

        lines.append("")

        lines.append(
            f"Decision: "
            f"{decision['decision']}"
        )

        lines.append(
            f"Reason: "
            f"{decision['reason']}"
        )

        lines.append(
            f"Impact: "
            f"{decision['impact']}"
        )

        lines.append(
            f"Stage: "
            f"{decision['stage']}"
        )

    return "\n".join(
        lines
    )