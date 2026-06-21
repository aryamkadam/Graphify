import subprocess


def get_project_evolution():

    stages = []

    try:

        tags = sorted(
            subprocess.check_output(
                ["git", "tag"],
                text=True
            ).splitlines()
        )

        for tag in tags:

            if not tag.startswith(
                "stage-"
            ):
                continue

            try:

                commit = subprocess.check_output(
                    [
                        "git",
                        "rev-list",
                        "-n",
                        "1",
                        tag
                    ],
                    text=True
                ).strip()

                stages.append(
                    {
                        "tag": tag,
                        "commit": commit[:7]
                    }
                )

            except Exception:
                pass

    except Exception:
        pass

    return stages