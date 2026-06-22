import subprocess


def get_contributor_ranking():

    ranking = {}

    try:

        authors = subprocess.check_output(
            [
                "git",
                "log",
                "--format=%an"
            ],
            text=True
        ).splitlines()

        for author in authors:

            ranking[
                author
            ] = ranking.get(
                author,
                0
            ) + 1

    except Exception:

        pass

    contributors = []

    for name, commits in sorted(
        ranking.items(),
        key=lambda x: x[1],
        reverse=True
    ):

        contributors.append({

            "name":
                name,

            "commits":
                commits
        })

    top_contributor = None

    if contributors:

        top_contributor = (
            contributors[0][
                "name"
            ]
        )

    return {

        "top_contributor":
            top_contributor,

        "contributors":
            contributors
    }