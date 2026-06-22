from graph_builder.github_activity import (
    get_commit_activity
)

from graph_builder.github_releases import (
    get_releases
)

from graph_builder.github_contributors import (
    get_contributors
)

from graph_builder.development_velocity import (
    get_development_velocity
)


def get_github_health():

    activity = (
        get_commit_activity()
    )

    releases = (
        get_releases()
    )

    contributors = (
        get_contributors()
    )

    velocity = (
        get_development_velocity()
    )

    score = 0

    score += activity[
        "activity_score"
    ]

    score += min(
        releases[
            "release_count"
        ] * 5,
        40
    )

    score += min(
        contributors[
            "count"
        ] * 10,
        20
    )

    score += min(
        int(
            velocity[
                "velocity_score"
            ] * 10
        ),
        20
    )

    score = min(
        score,
        100
    )

    if score >= 85:

        status = "EXCELLENT"

    elif score >= 70:

        status = "GOOD"

    elif score >= 50:

        status = "AVERAGE"

    else:

        status = "LOW"

    return {

        "github_health":
            status,

        "score":
            score
    }