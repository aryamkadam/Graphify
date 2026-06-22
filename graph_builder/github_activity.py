import subprocess


def get_commit_activity():

    commits = 0

    try:

        commits = int(
            subprocess.check_output(
                [
                    "git",
                    "rev-list",
                    "--count",
                    "HEAD"
                ],
                text=True
            ).strip()
        )

    except Exception:

        pass

    activity = {

        "total_commits":
            commits,

        "activity_score":
            min(
                commits * 10,
                100
            )
    }

    return activity