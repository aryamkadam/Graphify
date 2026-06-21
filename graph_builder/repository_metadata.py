import subprocess


def _run_git_command(command):

    try:

        result = subprocess.check_output(
            command,
            shell=True,
            text=True
        )

        return result.strip()

    except Exception:

        return "unknown"


def get_repository_metadata():

    latest_commit = _run_git_command(
        "git rev-parse --short HEAD"
    )

    total_commits = _run_git_command(
        "git rev-list --count HEAD"
    )

    latest_tag = _run_git_command(
        "git describe --tags --abbrev=0"
    )

    current_branch = _run_git_command(
        "git branch --show-current"
    )

    metadata = {

        "current_stage":
            latest_tag,

        "latest_commit":
            latest_commit,

        "total_commits":
            int(total_commits)
            if str(total_commits).isdigit()
            else 0,

        "latest_tag":
            latest_tag,

        "current_branch":
            current_branch
    }

    return metadata