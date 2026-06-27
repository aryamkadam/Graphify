import os
import ast


class EntryPointDetector:

    """
    Detects execution entry points
    inside a repository.
    """

    def __init__(self, repository_path):

        self.repository_path = repository_path

    def detect(self):

        entry_points = []

        ignored = {
            "__pycache__",
            ".git",
            ".venv",
            "node_modules"
        }

        for root, dirs, files in os.walk(self.repository_path):

            dirs[:] = [
                d for d in dirs
                if d not in ignored
            ]

            for file in files:

                if not file.endswith(".py"):
                    continue

                path = os.path.join(root, file)

                try:

                    with open(
                        path,
                        "r",
                        encoding="utf-8"
                    ) as f:

                        source = f.read()

                    tree = ast.parse(source)

                    for node in ast.walk(tree):

                        if isinstance(node, ast.If):

                            if (
                                isinstance(node.test, ast.Compare)
                                and isinstance(node.test.left, ast.Name)
                                and node.test.left.id == "__name__"
                            ):

                                entry_points.append({

                                    "file": path,

                                    "entry_type": "__main__"

                                })

                except Exception:

                    continue

        return entry_points