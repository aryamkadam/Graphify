from graph_builder.architecture_risks import (
    detect_single_points_of_failure
)

from graph_builder.dead_code import (
    detect_dead_code
)

from graph_builder.god_file_detector import (
    detect_god_files
)


def generate_risk_report(
    symbol_index
):

    return {

        "single_points_of_failure":
        detect_single_points_of_failure(
            symbol_index
        ),

        "dead_code":
        detect_dead_code(
            symbol_index
        ),

        "god_files":
        detect_god_files(
            symbol_index,
            threshold=2
        )
    }