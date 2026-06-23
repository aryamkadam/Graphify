from graph_builder.context_simulation import (
    simulate_change
)


def export_simulation_report(
    context,
    symbol
):

    result = simulate_change(
        context,
        symbol
    )

    lines = []

    lines.append(
        "# Context Simulation Report"
    )

    lines.append("")

    lines.append(
        f"Target Symbol: "
        f"{result['symbol']}"
    )

    lines.append(
        f"Risk Level: "
        f"{result['risk_level']}"
    )

    lines.append(
        f"Affected Symbols: "
        f"{result['affected_symbols']}"
    )

    lines.append(
        f"Recommendation: "
        f"{result['recommendation']}"
    )

    return "\n".join(
        lines
    )