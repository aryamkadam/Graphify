from graph_builder.context_execution_planner import (
    generate_execution_plan
)


def export_execution_plan(
    context
):

    plan = (
        generate_execution_plan(
            context
        )
    )

    lines = []

    lines.append(
        "# Execution Plan"
    )

    lines.append("")

    for item in plan:

        lines.append(

            f"Step {item['step']}"

        )

        lines.append(

            f"Action: "
            f"{item['action']}"

        )

        lines.append(

            f"Priority: "
            f"{item['priority']}"

        )

        lines.append(

            f"Expected Gain: "
            f"{item['expected_gain']}"

        )

        lines.append("")

    return "\n".join(
        lines
    )