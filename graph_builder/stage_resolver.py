import subprocess


def _run_git(command):

    try:

        result = subprocess.check_output(
            command,
            text=True
        )

        return result.strip()

    except Exception:

        return None


def resolve_current_stage():

    latest_tag = _run_git(

        [
            "git",
            "describe",
            "--tags",
            "--abbrev=0"
        ]

    )

    if latest_tag:

        return latest_tag

    branch = _run_git(

        [
            "git",
            "branch",
            "--show-current"
        ]

    )

    if branch:

        return f"development-{branch}"

    return "stage-unknown"


def is_stable_release():

    stage = (
        resolve_current_stage()
    )

    return stage.endswith(
        "-stable"
    )


def get_stage_family():

    stage = (
        resolve_current_stage()
    )

    parts = stage.split(
        "-"
    )

    if len(parts) >= 2:

        return parts[1]

    return "unknown"