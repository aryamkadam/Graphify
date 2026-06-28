"""
Stage 15.5

Repository Story Engine

Builds the evolution story
of the repository.

Compatible with the NEW Repository Brain.
"""


class RepositoryStoryEngine:

    def __init__(self, intelligence):

        self.intelligence = intelligence

    # ---------------------------------------------

    def _project_age(self):

        metadata = self.intelligence.get(
            "metadata",
            {}
        )

        commits = metadata.get(
            "total_commits",
            0
        )

        if commits < 20:

            return (
                "Project is in its initial phase."
            )

        elif commits < 100:

            return (
                "Project has entered a stable development phase."
            )

        elif commits < 300:

            return (
                "Project has become a mature software system."
            )

        return (
            "Project has a long and rich development history."
        )

    # ---------------------------------------------

    def _development_style(self):

        score = self.intelligence.get(
            "health",
            {}
        ).get(
            "health_score",
            0
        )

        if score >= 90:

            return (
                "Development appears disciplined and well maintained."
            )

        elif score >= 75:

            return (
                "Development appears active with good engineering practices."
            )

        elif score >= 50:

            return (
                "Development is progressing but technical debt is growing."
            )

        return (
            "Development requires significant refactoring."
        )

    # ---------------------------------------------

    def _repository_direction(self):

        insights = self.intelligence.get(
            "insights",
            {}
        )

        area = insights.get(
            "dominant_area",
            "Unknown"
        )

        return (
            f"The repository is currently evolving toward {area}."
        )

    # ---------------------------------------------

    def _future_prediction(self):

        score = self.intelligence.get(
            "health",
            {}
        ).get(
            "health_score",
            0
        )

        if score >= 90:

            return (
                "Repository is ready for enterprise-scale evolution."
            )

        elif score >= 70:

            return (
                "Repository can safely expand with new modules."
            )

        return (
            "Repository should improve its architecture before major expansion."
        )

    # ---------------------------------------------

    def build(self):

        return {

            "past":
                self._project_age(),

            "present":
                self._development_style(),

            "direction":
                self._repository_direction(),

            "future":
                self._future_prediction()

        }