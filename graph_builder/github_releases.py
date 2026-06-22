import subprocess


def get_releases():

    releases = []

    try:

        tags = subprocess.check_output(
            [
                "git",
                "tag"
            ],
            text=True
        ).splitlines()

        releases = sorted(tags)

    except Exception:

        pass

    return {

        "release_count":
            len(releases),

        "releases":
            releases
    }