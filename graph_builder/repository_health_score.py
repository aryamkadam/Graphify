from graph_builder.dead_code import (
    detect_dead_code
)

from graph_builder.risk_ranking import (
    rank_repository_risks
)

from graph_builder.god_file_detector import (
    detect_god_files
)

from graph_builder.hotspot_analysis import (
    detect_hotspots
)


def calculate_repository_health(
    symbol_index,
    knowledge_graph
):

    score = 100

    risks = rank_repository_risks(
        symbol_index,
        knowledge_graph
    )

    dead_code = detect_dead_code(
        symbol_index
    )

    god_files = detect_god_files(
        symbol_index
    )

    hotspots = detect_hotspots(
        symbol_index
    )

    score -= len(dead_code)

    score -= (
        len(god_files) * 5
    )

    high_risks = 0

    for risk in risks:

        if (
            risk["severity"]
            == "HIGH"
        ):
            high_risks += 1

    score -= (
        high_risks * 5
    )

    if score < 0:

        score = 0

    if score >= 85:

        status = "EXCELLENT"

    elif score >= 70:

        status = "GOOD"

    elif score >= 50:

        status = "FAIR"

    else:

        status = "POOR"

    return {
        "score": score,
        "status": status,
        "dead_code_count":
            len(dead_code),
        "god_files_count":
            len(god_files),
        "high_risk_symbols":
            high_risks,
        "hotspot_count":
            len(hotspots)
    }