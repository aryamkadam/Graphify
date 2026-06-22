def generate_context_diff(
    old_context,
    new_context
):

    old_stage = old_context[
        "project"
    ][
        "current_stage"
    ]

    new_stage = new_context[
        "project"
    ][
        "current_stage"
    ]

    old_commits = old_context[
        "project"
    ].get(
        "total_commits",
        0
    )

    new_commits = new_context[
        "project"
    ].get(
        "total_commits",
        0
    )

    old_health = old_context[
        "repository"
    ][
        "health_score"
    ]

    new_health = new_context[
        "repository"
    ][
        "health_score"
    ]

    old_features = set(
        old_context[
            "project"
        ].get(
            "future_features",
            []
        )
    )

    new_features = set(
        new_context[
            "project"
        ].get(
            "future_features",
            []
        )
    )

    added = list(
        new_features - old_features
    )

    removed = list(
        old_features - new_features
    )

    return {

        "old_stage":
            old_stage,

        "new_stage":
            new_stage,

        "commit_change":
            new_commits - old_commits,

        "health_change":
            new_health - old_health,

        "added_features":
            added,

        "removed_features":
            removed
    }