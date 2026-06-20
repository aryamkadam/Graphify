from graph_builder.dead_code import (
    detect_dead_code
)

from graph_builder.god_file_detector import (
    detect_god_files
)

from graph_builder.risk_ranking import (
    rank_repository_risks
)

from graph_builder.critical_symbol_ranking import (
    rank_critical_symbols
)


def generate_recommendations(
    symbol_index,
    knowledge_graph
):

    recommendations = []

    critical = rank_critical_symbols(
        symbol_index,
        knowledge_graph
    )

    if critical:

        recommendations.append(
            {
                "priority": "HIGH",
                "score":
                critical[0][
                    "critical_score"
                ] * 10,
                "message":
                f"Reduce dependency on "
                f"{critical[0]['symbol']}."
            }
        )

    risks = rank_repository_risks(
        symbol_index,
        knowledge_graph
    )

    if risks:

        recommendations.append(
            {
                "priority": "HIGH",
                "score":
                risks[0][
                    "impact_score"
                ] * 10,
                "message":
                f"Review high-risk symbol "
                f"{risks[0]['symbol']}."
            }
        )

    god_files = detect_god_files(
        symbol_index
    )

    for file_info in god_files[:3]:

        recommendations.append(
            {
                "priority": "MEDIUM",
                "score": 50,
                "message":
                f"Consider splitting "
                f"{file_info['file']}."
            }
        )

    dead_code = detect_dead_code(
        symbol_index
    )

    if dead_code:

        recommendations.append(
            {
                "priority": "LOW",
                "score":
                len(dead_code),
                "message":
                f"Remove or review "
                f"{len(dead_code)} dead symbols."
            }
        )

    recommendations.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return recommendations