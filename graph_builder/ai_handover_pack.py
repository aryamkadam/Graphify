from graph_builder.repository_brain import (
    generate_repository_brain
)


def generate_ai_handover_pack(
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
        "# Graphify AI Handover Pack"
    )

    lines.append("")

    lines.append(
        "## Project Purpose"
    )

    lines.append("")
    lines.append(
        "Graphify is an AI Context Transfer Engine."
    )

    lines.append(
        "It solves the problem of losing project context"
    )

    lines.append(
        "when switching between AI systems."
    )

    lines.append("")

    lines.append(
        "## Current Development Status"
    )

    lines.append("")

    lines.append(
        "Stage 5 Complete"
    )

    lines.append("")

    lines.append(
        "Completed Modules:"
    )

    lines.append(
        "- Repository Scanner"
    )

    lines.append(
        "- Symbol Index"
    )

    lines.append(
        "- Knowledge Graph"
    )

    lines.append(
        "- Dependency Explorer"
    )

    lines.append(
        "- Impact Analysis"
    )

    lines.append(
        "- Risk Ranking"
    )

    lines.append(
        "- Critical Symbol Ranking"
    )

    lines.append(
        "- Repository Health Engine"
    )

    lines.append(
        "- Repository Brain Generator"
    )

    lines.append(
        "- Context Pack Generator"
    )

    lines.append("")

    lines.append(
        "## Repository Health"
    )

    lines.append("")

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

    lines.append("")

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

    lines.append("")

    for symbol in brain[
        "risky_symbols"
    ]:

        lines.append(
            f"- {symbol}"
        )

    lines.append("")

    lines.append(
        "## Existing Outputs"
    )

    lines.append("")

    lines.append(
        "- symbol_index.json"
    )

    lines.append(
        "- repository_dashboard.json"
    )

    lines.append(
        "- repository_brain.json"
    )

    lines.append(
        "- repository_context.md"
    )

    lines.append("")

    lines.append(
        "## Rules For Future Development"
    )

    lines.append("")

    lines.append(
        "Do not rebuild completed intelligence modules."
    )

    lines.append(
        "Extend existing architecture."
    )

    lines.append("")

    lines.append(
        "## Recommended Next Steps"
    )

    lines.append("")

    lines.append(
        "- Improve Repository Brain"
    )

    lines.append(
        "- Generate Architecture Summaries"
    )

    lines.append(
        "- AI Conversation Memory Export"
    )

    lines.append(
        "- GitHub Integration"
    )

    lines.append(
        "- VS Code Extension"
    )

    lines.append("")

    lines.append(
        "## AI Instruction"
    )

    lines.append("")

    lines.append(
        "Continue development from Stage 6."
    )

    lines.append(
        "Treat Stage 5 as stable and complete."
    )

    return "\n".join(
        lines
    )