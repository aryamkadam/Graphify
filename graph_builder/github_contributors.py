import subprocess


def get_contributors():

    contributors = []

    try:

        output = subprocess.check_output(
            [
                "git",
                "log",
                "--format=%an"
            ],
            text=True
        )

        names = set(
            output.splitlines()
        )

        for name in sorted(names):

            contributors.append(
                name
            )

    except Exception:

        pass

    return {

        "contributors":
            contributors,

        "count":
            len(contributors)
    }