from graph_builder.context_reasoning import (
    ask_context_reason
)


def export_reasoning_report(
    context,
    question
):

    result = ask_context_reason(
        context,
        question
    )

    lines = []

    lines.append(
        "# Context Reasoning Report"
    )

    lines.append("")

    lines.append(
        f"Question: {result['question']}"
    )

    lines.append("")

    lines.append(
        f"Answer: {result['answer']}"
    )

    return "\n".join(
        lines
    )