from graph_builder.context_forecast import (
    generate_forecast
)


def export_forecast_report(
    context
):

    forecast = (
        generate_forecast(
            context
        )
    )

    lines = []

    lines.append(
        "# Context Forecast Report"
    )

    lines.append("")

    lines.append(
        f"Current Health: "
        f"{forecast['current_health']}"
    )

    lines.append(
        f"After Dead Code Removal: "
        f"{forecast['after_dead_code_removal']}"
    )

    lines.append(
        f"After Refactoring: "
        f"{forecast['after_refactoring']}"
    )

    lines.append(
        f"After Hotspot Reduction: "
        f"{forecast['after_hotspot_reduction']}"
    )

    lines.append(
        f"Predicted Final Health: "
        f"{forecast['predicted_final_health']}"
    )

    return "\n".join(
        lines
    )