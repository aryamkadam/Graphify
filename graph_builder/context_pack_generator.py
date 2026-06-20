from graph_builder.repository_brain import (
    generate_repository_brain
)


def generate_context_pack(
    symbol_index,
    knowledge_graph
):

    brain = generate_repository_brain(
        symbol_index,
        knowledge_graph,
        project_name="Graphify",
        project_purpose=
        "AI Context Transfer Engine",
        current_stage=
        "Stage 5 Complete"
    )

    lines = []

    lines.append(
        "# Repository Context"
    )

    lines.append("")

    lines.append(
        f"Project Name: "
        f"{brain['project_name']}"
    )

    lines.append(
        f"Purpose: "
        f"{brain['project_purpose']}"
    )

    lines.append(
        f"Current Stage: "
        f"{brain['current_stage']}"
    )

    lines.append("")

    lines.append(
        "## Repository Health"
    )

    lines.append(
        f"Health Score: "
        f"{brain['health_score']}"
    )

    lines.append(
        f"Status: "
        f"{brain['status']}"
    )

    lines.append("")

    lines.append(
        "## Critical Symbols"
    )

    for symbol in brain[
        "critical_symbols"
    ]:

        lines.append(
            f"- {symbol}"
        )

    lines.append("")

    lines.append(
        "## Risky Symbols"
    )

    for symbol in brain[
        "risky_symbols"
    ]:

        lines.append(
            f"- {symbol}"
        )

    lines.append("")

    lines.append(
        "## Repository Statistics"
    )

    lines.append(
        f"Dead Code Count: "
        f"{brain['dead_code_count']}"
    )

    lines.append(
        f"Hotspot Count: "
        f"{brain['hotspot_count']}"
    )

    lines.append("")

    lines.append(
        "## Top Recommendations"
    )

    for recommendation in brain[
        "top_recommendations"
    ]:

        lines.append(
            f"- {recommendation['message']}"
        )

    lines.append("")

    lines.append(
        "## AI Instructions"
    )

    lines.append(
        "Continue development "
        "without rebuilding "
        "existing intelligence modules."
    )

    return "\n".join(
        lines
    )