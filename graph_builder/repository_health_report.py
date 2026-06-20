from graph_builder.repository_health_score import (
    calculate_repository_health
)

from graph_builder.refactoring_recommendations import (
    generate_recommendations
)


def generate_health_report(
    symbol_index,
    knowledge_graph
):

    health = (
        calculate_repository_health(
            symbol_index,
            knowledge_graph
        )
    )

    recommendations = (
        generate_recommendations(
            symbol_index,
            knowledge_graph
        )
    )

    report = {
        "health_score":
            health["score"],

        "status":
            health["status"],

        "dead_code":
            health["dead_code_count"],

        "god_files":
            health["god_files_count"],

        "high_risk_symbols":
            health["high_risk_symbols"],

        "top_recommendations":
            recommendations[:5]
    }

    return report