from graph_builder.ai_context_pack import (
    build_ai_context_pack
)

from graph_builder.prediction_engine import (
    generate_prediction
)


def generate_ai_handover_pack(
    symbol_index,
    knowledge_graph
):

    context = build_ai_context_pack(
    symbol_index,
    knowledge_graph
)

    repo = context["repository_brain"]

    project = context["project_memory"]

    github = context["github_intelligence"]

    decision = context["decision_brain"]

    session = context["session_memory"]

    prediction = generate_prediction(
    repo
 )
    lines = []

    lines.append(
        "# Graphify AI Handover Pack"
    )

    lines.append("")
    lines.append("## Project Overview")
    lines.append("")

    lines.append(
        f"Project: {project['project_name']}"
    )

    lines.append(
        f"Goal: {project['goal']}"
    )

    lines.append(
        f"Current Stage: {project['current_stage']}"
    )

    lines.append(
        f"Latest Commit: {project['latest_commit']}"
    )

    lines.append("")

    lines.append(
        "## Repository Health"
    )

    lines.append("")

    lines.append(
        f"Health Score: {repo['health_score']}"
    )

    lines.append(
        f"Status: {repo['status']}"
    )

    lines.append(
        f"Dead Code Count: {repo['dead_code_count']}"
    )

    lines.append(
        f"Hotspot Count: {repo['hotspot_count']}"
    )

    lines.append("")

    lines.append(
        "## Critical Symbols"
    )

    lines.append("")

    for symbol in repo["critical_symbols"]:

        lines.append(
            f"- {symbol}"
        )

    lines.append("")

    lines.append(
        "## Important Decisions"
    )

    lines.append("")

    for item in decision["latest_decisions"]:

        lines.append(
            f"- {item['title']}"
        )

    lines.append("")

    lines.append(
        "## GitHub Intelligence"
    )

    lines.append("")

    lines.append(
        f"Repository Maturity: "
        f"{github['maturity']['maturity_level']}"
    )

    lines.append(
        f"GitHub Health: "
        f"{github['github_health']['github_health']}"
    )

    lines.append(
        f"Total Commits: "
        f"{github['activity']['total_commits']}"
    )

    lines.append("")

    lines.append(
        "## AI Session Memory"
    )

    lines.append("")

    lines.append(
        f"Latest Focus: "
        f"{session['latest_focus']}"
    )

    lines.append(
        f"Total Sessions: "
        f"{session['total_sessions']}"
    )

    lines.append("")

    lines.append(
        "## Future Roadmap"
    )

    lines.append("")

    lines.append(
        f"Recommended Next Stage: "
        f"{prediction['recommended_next_stage']}"
    )

    lines.append(
        f"Recommended Feature: "
        f"{prediction['recommended_feature']}"
    )

    lines.append("")

    lines.append(
        "## Instructions For Next AI"
    )

    lines.append("")

    lines.append(
        "Continue development without rebuilding completed engines."
    )

    lines.append(
        "Use Repository Brain as source of truth."
    )

    lines.append(
        "Use Project Memory for roadmap continuity."
    )

    lines.append(
        "Use Decision Brain for architectural reasoning."
    )

    return "\n".join(
        lines
    )