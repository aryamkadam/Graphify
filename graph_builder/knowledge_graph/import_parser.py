"""
Import Relationship Engine

Stage 14.3

Builds dependency relationships
between Python files.
"""

import ast
import os


class ImportParser:

    def __init__(self, repository_path):

        self.repository_path = repository_path


    def parse_imports(self):

        edges = []

        ignored_dirs = {
            "__pycache__",
            ".git",
            ".venv",
            "node_modules"
        }

        for root, dirs, files in os.walk(self.repository_path):

            dirs[:] = [
                d for d in dirs
                if d not in ignored_dirs
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

                        tree = ast.parse(f.read())

                    for node in ast.walk(tree):

                        if isinstance(node, ast.Import):

                            for module in node.names:

                                edges.append({

                                    "source": path,

                                    "target": module.name,

                                    "type": "import"
                                })

                        elif isinstance(node, ast.ImportFrom):

                            if node.module:

                                edges.append({

                                    "source": path,

                                    "target": node.module,

                                    "type": "from_import"
                                })

                except Exception:

                    continue

        return edges