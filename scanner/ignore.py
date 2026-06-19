from pathlib import Path
import pathspec


def load_ignore_patterns(root_path):

    patterns = []

    gitignore = Path(root_path) / ".gitignore"

    if gitignore.exists():

        with open(
            gitignore,
            "r",
            encoding="utf-8"
        ) as f:

            patterns.extend(
                f.readlines()
            )

    graphifyignore = (
        Path(root_path)
        / ".graphifyignore"
    )

    if graphifyignore.exists():

        with open(
            graphifyignore,
            "r",
            encoding="utf-8"
        ) as f:

            patterns.extend(
                f.readlines()
            )

    if not patterns:
        return None

    return pathspec.PathSpec.from_lines(
        "gitwildmatch",
        patterns
    )