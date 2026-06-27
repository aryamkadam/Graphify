"""
Function Call Parser

Stage 14.5

Detects function calls
between repository files.
"""

import ast
import os


class FunctionCallParser:

    def __init__(self, repository_path):

        self.repository_path = repository_path


    def parse(self):

        calls = []

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

                filepath = os.path.join(root, file)

                try:

                    with open(
                        filepath,
                        "r",
                        encoding="utf-8"
                    ) as f:

                        tree = ast.parse(f.read())

                    current_function = None

                    for node in ast.walk(tree):

                        if isinstance(node, ast.FunctionDef):

                            current_function = node.name

                        elif isinstance(node, ast.Call):

                            if isinstance(node.func, ast.Name):

                                calls.append({

                                    "source_file": filepath,

                                    "source_function": current_function,

                                    "target_function": node.func.id,

                                    "type": "call"

                                })

                except Exception:

                    continue

        return calls