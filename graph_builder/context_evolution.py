from graph_builder.context_diff import (
    generate_context_diff
)


def generate_context_evolution(
    old_context,
    new_context
):

    diff = generate_context_diff(
        old_context,
        new_context
    )

    evolution = {

        "old_stage":
            diff["old_stage"],

        "new_stage":
            diff["new_stage"],

        "growth_summary": {

            "health_change":
                diff["health_change"],

            "commit_change":
                diff["commit_change"]
        },

        "new_capabilities":
            diff["added_features"],

        "removed_capabilities":
            diff["removed_features"],

        "evolution_status":
            "EVOLVED"
    }

    return evolution