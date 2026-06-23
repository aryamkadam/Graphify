from graph_builder.context_advisor import (
    generate_context_advice
)


def export_context_advice(
    context
):

    advice = (
        generate_context_advice(
            context
        )
    )

    lines = []

    lines.append(
        "# Context Advisor"
    )

    lines.append("")

    lines.append(
        f"Next Action: "
        f"{advice['next_action']}"
    )

    lines.append(
        f"Priority: "
        f"{advice['priority']}"
    )

    lines.append(
        f"Expected Gain: "
        f"{advice['expected_gain']}"
    )

    lines.append(
        f"Reason: "
        f"{advice['reason']}"
    )

    return "\n".join(
        lines
    )