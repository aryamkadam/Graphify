from graph_builder.architecture_risks import (
    detect_single_points_of_failure
)

from graph_builder.dead_code import (
    detect_dead_code
)

from graph_builder.god_file_detector import (
    detect_god_files
)


def calculate_health_score(
    symbol_index
):

    score = 100

    spof = detect_single_points_of_failure(
        symbol_index
    )

    dead_code = detect_dead_code(
        symbol_index
    )

    god_files = detect_god_files(
        symbol_index,
        threshold=2
    )

    score -= len(spof) * 5

    score -= len(god_files) * 2

    score -= len(dead_code)

    score = max(
        score,
        0
    )

    return score


def determine_risk_level(
    score
):

    if score >= 90:
        return "EXCELLENT"

    if score >= 75:
        return "GOOD"

    if score >= 60:
        return "MODERATE"

    if score >= 40:
        return "HIGH_RISK"

    return "CRITICAL"


def generate_health_report(
    symbol_index
):

    score = calculate_health_score(
        symbol_index
    )

    return {

        "health_score": score,

        "risk_level":
        determine_risk_level(
            score
        ),

        "dead_code_count":
        len(
            detect_dead_code(
                symbol_index
            )
        ),

        "god_file_count":
        len(
            detect_god_files(
                symbol_index,
                threshold=2
            )
        ),

        "single_point_count":
        len(
            detect_single_points_of_failure(
                symbol_index
            )
        )
    }


def generate_recommendations(
    symbol_index
):

    recommendations = []

    dead_code = detect_dead_code(
        symbol_index
    )

    if dead_code:

        recommendations.append(
            f"Remove or review {len(dead_code)} dead symbols."
        )

    god_files = detect_god_files(
        symbol_index,
        threshold=2
    )

    for file in god_files:

        recommendations.append(
            f"Consider splitting {file['file']}."
        )

    spof = detect_single_points_of_failure(
        symbol_index
    )

    for item in spof:

        recommendations.append(
            f"Reduce dependency on {item['symbol']}."
        )

    return recommendations


def generate_executive_summary(
    symbol_index
):

    report = generate_health_report(
        symbol_index
    )

    recommendations = (
        generate_recommendations(
            symbol_index
        )
    )

    return {

        "report": report,

        "recommendations":
        recommendations
    }