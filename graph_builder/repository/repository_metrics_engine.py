"""
Graphify

Phase 9

Stage P9.4

Repository Metrics Engine

Computes objective engineering metrics
from RepositoryKnowledge.

Author:
Graphify Core
"""


class RepositoryMetricsEngine:

    VERSION = "P9.4"

    def analyze(self, knowledge):

        module_count = len(knowledge.modules)
        file_count = len(knowledge.files)
        directory_count = len(knowledge.directories)

        if module_count == 0:
            avg_files_per_module = 0
        else:
            avg_files_per_module = round(
                file_count / module_count,
                2,
            )

        # -----------------------------------------

        if file_count < 20:
            repository_size = "SMALL"
        elif file_count < 100:
            repository_size = "MEDIUM"
        else:
            repository_size = "LARGE"

        # -----------------------------------------

        if avg_files_per_module <= 3:
            complexity = "LOW"
        elif avg_files_per_module <= 8:
            complexity = "MEDIUM"
        else:
            complexity = "HIGH"

        # -----------------------------------------

        if complexity == "LOW":
            health = "GOOD"
        elif complexity == "MEDIUM":
            health = "STABLE"
        else:
            health = "ATTENTION_REQUIRED"

        return {

            "repository_size": repository_size,

            "directories": directory_count,

            "files": file_count,

            "modules": module_count,

            "average_files_per_module": avg_files_per_module,

            "complexity": complexity,

            "health": health,

            "version": self.VERSION,

        }