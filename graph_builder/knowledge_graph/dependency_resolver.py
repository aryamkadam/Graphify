"""
Dependency Resolver

Stage 14.4

Converts imported module names
into actual repository files.
"""

import os


class DependencyResolver:

    def __init__(self, repository_path):

        self.repository_path = repository_path

        self.module_map = {}

        self.build_module_index()


    def build_module_index(self):

        """
        Build:

        graph_builder.context_builder

                ↓

        graph_builder/context_builder.py
        """

        for root, dirs, files in os.walk(self.repository_path):

            if "__pycache__" in root:
                continue

            for file in files:

                if not file.endswith(".py"):
                    continue

                full_path = os.path.join(root, file)

                relative = os.path.relpath(
                    full_path,
                    self.repository_path
                )

                module = (
                    relative
                    .replace("\\", ".")
                    .replace("/", ".")
                    .replace(".py", "")
                )

                self.module_map[module] = full_path


    def resolve(self, edges):

        resolved = []

        for edge in edges:

            target = edge["target"]

            if target in self.module_map:

                resolved.append({

                    "source": edge["source"],

                    "target": self.module_map[target],

                    "type": edge["type"],

                    "resolved": True
                })

            else:

                resolved.append({

                    "source": edge["source"],

                    "target": target,

                    "type": edge["type"],

                    "resolved": False
                })

        return resolved