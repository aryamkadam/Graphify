from graph_builder.github_releases import (
    get_releases
)

from graph_builder.github_activity import (
    get_commit_activity
)


def calculate_repository_maturity():

    releases = (
        get_releases()
    )

    activity = (
        get_commit_activity()
    )

    score = 0

    score += releases[
        "release_count"
    ] * 10

    score += activity[
        "total_commits"
    ] * 3

    score = min(
        score,
        100
    )

    if score >= 80:

        level = "ADVANCED"

    elif score >= 60:

        level = "MATURE"

    elif score >= 30:

        level = "GROWING"

    else:

        level = "EARLY"

    return {

        "maturity_score":
            score,

        "maturity_level":
            level
    }