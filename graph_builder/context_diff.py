def generate_context_diff(
    old_context,
    new_context
):

    old_identity = old_context[
        "identity"
    ]

    new_identity = new_context[
        "identity"
    ]

    old_quality = old_context[
        "quality"
    ]

    new_quality = new_context[
        "quality"
    ]

    old_stage = old_identity[
        "current_stage"
    ]

    new_stage = new_identity[
        "current_stage"
    ]

    old_score = old_quality.get(
        "transfer_score",
        0
    )

    new_score = new_quality.get(
        "transfer_score",
        0
    )

    old_actions = set(
        old_context[
            "continuation"
        ].get(
            "recommended_actions",
            []
        )
    )

    new_actions = set(
        new_context[
            "continuation"
        ].get(
            "recommended_actions",
            []
        )
    )

    added = list(
        new_actions - old_actions
    )

    removed = list(
        old_actions - new_actions
    )

    return {

        "old_stage":
            old_stage,

        "new_stage":
            new_stage,

        "transfer_score_change":
            new_score - old_score,

        "added_actions":
            added,

        "removed_actions":
            removed
    }