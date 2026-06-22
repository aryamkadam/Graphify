from graph_builder.ai_context_pack import (
    build_ai_context_pack
)

from graph_builder.prediction_engine import (
    generate_prediction
)


def generate_ai_handover_summary(
    symbol_index,
    knowledge_graph
):

    context_pack = (
        build_ai_context_pack(
            symbol_index,
            knowledge_graph
        )
    )

    prediction = (
        generate_prediction(
            symbol_index,
            knowledge_graph
        )
    )

    repo = context_pack[
        "repository_brain"
    ]

    github = context_pack[
        "github_intelligence"
    ]

    summary = f"""
# Graphify AI Handover

Project:
{repo['project_name']}

Purpose:
{repo['project_purpose']}

Current Stage:
{repo['current_stage']}

Latest Commit:
{repo['latest_commit']}

Health Score:
{repo['health_score']}

Repository Status:
{repo['status']}

Project Direction:
{repo['project_direction']}

Most Important Decision:
{repo['most_important_decision']['title']}

GitHub Health:
{github['github_health']['github_health']}

Repository Maturity:
{github['maturity']['maturity_level']}

Recommended Next Stage:
{prediction['recommended_next_stage']}

Recommended Feature:
{prediction['recommended_feature']}

Instructions:
Continue development without rebuilding
completed engines.
"""

    return summary