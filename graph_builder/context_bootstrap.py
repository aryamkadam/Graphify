from graph_builder.context_history import (
    get_context_history
)

from graph_builder.decision_summary import (
    generate_decision_summary
)


def generate_context_bootstrap(
    context
):

    history = get_context_history()

    decision_summary = (
        generate_decision_summary()
    )

    lines = []

    lines.append(
        "=== GRAPHIFY AI BOOTSTRAP ==="
    )

    lines.append("")

    lines.append(
        f"Project: {context['project_name']}"
    )

    lines.append(
        f"Current Stage: {context['stage']}"
    )

    lines.append(
        f"Repository Health: {context['health_score']}"
    )

    lines.append("")

    lines.append(
        "Project Goal:"
    )

    lines.append(
        "Graphify = Git for AI Context"
    )

    lines.append("")

    lines.append(
        "Purpose:"
    )

    lines.append(
        "Preserve, transfer and restore AI understanding."
    )

    lines.append("")

    lines.append(
        "Project Evolution:"
    )

    for item in history:

        lines.append(

            f"- {item.get('timestamp','')} | "
            f"{item.get('message','')}"
        )

    lines.append("")

    lines.append(
        f"Total Context Commits: {len(history)}"
    )

    lines.append("")

    lines.append(
        "Key Decisions:"
    )

    for decision in decision_summary:

        lines.append(
            f"- {decision}"
        )

    lines.append("")

    lines.append(
        "Important Decision:"
    )

    lines.append(
        "Focus on AI Context Transfer, not repository analytics."
    )

    lines.append("")

    lines.append(
        "Current Focus:"
    )

    lines.append(
        "AI Memory Infrastructure"
    )

    lines.append("")

    lines.append(
        "Recommended Next Step:"
    )

    lines.append(
        "Improve AI Context Continuation."
    )

    lines.append("")

    lines.append(
        "Continue development from this state."
    )

    return "\n".join(
        lines
    )