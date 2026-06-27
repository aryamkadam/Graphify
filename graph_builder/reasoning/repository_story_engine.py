"""
Stage 15.5

Repository Story Engine

Builds the evolution story of the repository.

Instead of showing only repository facts,
Graphify starts understanding the project's journey.

Future AI agents will use this
to understand how the software evolved.
"""


class RepositoryStoryEngine:

    def __init__(self, intelligence):

        self.intelligence = intelligence

    # ---------------------------------------------

    def _project_age(self):

        commits = self.intelligence["identity"]["total_commits"]

        if commits < 20:

            return "Project is in its initial phase."

        elif commits < 100:

            return "Project has entered a stable development phase."

        elif commits < 300:

            return "Project has become a mature software system."

        return "Project has a long and rich development history."

    # ---------------------------------------------

    def _development_style(self):

        health = self.intelligence["health"]["health_score"]

        if health >= 90:

            return "Development appears disciplined and well maintained."

        elif health >= 75:

            return "Development appears active with good engineering practices."

        elif health >= 50:

            return "Development is progressing but technical debt is growing."

        return "Development requires significant refactoring."

    # ---------------------------------------------

    def _repository_direction(self):

        area = self.intelligence["decisions"]["insights"]["dominant_area"]

        return f"The repository is currently evolving toward {area}."

    # ---------------------------------------------

    def _future_prediction(self):

        health = self.intelligence["health"]["health_score"]

        if health >= 90:

            return (
                "Repository is ready for enterprise-scale evolution."
            )

        elif health >= 70:

            return (
                "Repository can safely expand with new modules."
            )

        return (
            "Repository should improve its architecture before major expansion."
        )

    # ---------------------------------------------

    def build(self):

        story = {

            "past": self._project_age(),

            "present": self._development_style(),

            "direction": self._repository_direction(),

            "future": self._future_prediction()

        }

        return story