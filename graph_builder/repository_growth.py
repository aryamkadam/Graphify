from graph_builder.github_activity import (
    get_commit_activity
)

from graph_builder.github_releases import (
    get_releases
)


def get_repository_growth():

    activity = (
        get_commit_activity()
    )

    releases = (
        get_releases()
    )

    commits = activity[
        "total_commits"
    ]

    release_count = releases[
        "release_count"
    ]

    if commits >= 10:

        growth_status = "FAST"

    elif commits >= 5:

        growth_status = "MEDIUM"

    else:

        growth_status = "EARLY"

    return {

        "growth_status":
            growth_status,

        "commit_count":
            commits,

        "release_count":
            release_count
    }