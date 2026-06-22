from graph_builder.github_activity import (
    get_commit_activity
)

from graph_builder.github_releases import (
    get_releases
)


def get_development_velocity():

    activity = (
        get_commit_activity()
    )

    releases = (
        get_releases()
    )

    total_commits = activity[
        "total_commits"
    ]

    total_releases = max(
        releases[
            "release_count"
        ],
        1
    )

    velocity_score = round(
        total_commits /
        total_releases,
        2
    )

    return {

        "total_commits":
            total_commits,

        "total_releases":
            total_releases,

        "velocity_score":
            velocity_score
    }