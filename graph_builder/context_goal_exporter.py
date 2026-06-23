from graph_builder.context_goal import (
    generate_goal_plan
)


def export_goal_report(
    context,
    target_health=95
):

    plan = (
        generate_goal_plan(
            context,
            target_health
        )
    )

    lines = []

    lines.append(
        "# Context Goal Report"
    )

    lines.append("")

    lines.append(
        f"Current Health: "
        f"{plan['current_health']}"
    )

    lines.append(
        f"Target Health: "
        f"{plan['target_health']}"
    )

    lines.append(
        f"Health Gap: "
        f"{plan['health_gap']}"
    )

    lines.append(
        f"Predicted Health: "
        f"{plan['predicted_health']}"
    )

    lines.append(
        f"Success Probability: "
        f"{plan['success_probability']}%"
    )

    lines.append("")
    lines.append("Required Actions")
    lines.append("")

    for index, action in enumerate(
        plan[
            "required_actions"
        ],
        start=1
    ):

        lines.append(
            f"{index}. {action}"
        )

    return "\n".join(
        lines
    )