from graph_builder.github_activity import (
    get_commit_activity
)

from graph_builder.github_contributors import (
    get_contributors
)

from graph_builder.github_releases import (
    get_releases
)

from graph_builder.development_velocity import (
    get_development_velocity
)

from graph_builder.contributor_ranking import (
    get_contributor_ranking
)

from graph_builder.repository_growth import (
    get_repository_growth
)

from graph_builder.github_health import (
    get_github_health
)

from graph_builder.repository_maturity import (
    calculate_repository_maturity
)


def generate_github_intelligence():

    activity = (
        get_commit_activity()
    )

    contributors = (
        get_contributors()
    )

    releases = (
        get_releases()
    )

    velocity = (
        get_development_velocity()
    )

    ranking = (
        get_contributor_ranking()
    )

    growth = (
        get_repository_growth()
    )

    health = (
        get_github_health()
    )

    maturity_data = (
        calculate_repository_maturity()
    )

    maturity = "LOW"

    if releases[
        "release_count"
    ] >= 5:

        maturity = "HIGH"

    elif releases[
        "release_count"
    ] >= 2:

        maturity = "MEDIUM"

    return {

        "activity":
            activity,

        "contributors":
            contributors,

        "releases":
            releases,

        "velocity":
            velocity,

        "contributor_ranking":
            ranking,

        "growth":
            growth,

        "github_health":
            health,

        "maturity":
            maturity_data,

        "repository_maturity":
            maturity
    }