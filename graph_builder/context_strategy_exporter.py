from graph_builder.context_strategy import (
    generate_strategy
)


def export_strategy_report(
    context,
    target_health=90
):

    strategy = (
        generate_strategy(
            context,
            target_health
        )
    )

    lines = []

    lines.append(
        "# Context Strategy Report"
    )

    lines.append("")

    lines.append(
        f"Current Health: "
        f"{strategy['current_health']}"
    )

    lines.append(
        f"Target Health: "
        f"{strategy['target_health']}"
    )

    lines.append(
        f"Estimated Effort: "
        f"{strategy['estimated_effort']}"
    )

    lines.append("")

    lines.append(
        "## Strategy Steps"
    )

    lines.append("")

    for item in strategy[
        "strategy_steps"
    ]:

        lines.append(

            f"{item['step']}. "
            f"{item['action']} "
            f"({item['priority']})"
        )

    return "\n".join(
        lines
    )