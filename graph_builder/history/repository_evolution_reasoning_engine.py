"""
Stage 16.4

Repository Evolution Reasoning Engine

Transforms repository evolution data into
high-level engineering understanding.

This engine explains WHAT changed
and WHY it matters.

Future AI agents will use this
instead of raw evolution metrics.
"""


class RepositoryEvolutionReasoningEngine:

    def __init__(self, evolution_report):

        self.report = evolution_report

    # ---------------------------------------------

    def _health_reasoning(self):

        health = self.report.get("health", {})

        status = health.get("status", "unchanged")

        if status == "improved":

            return (
                "Repository health is steadily improving, "
                "indicating successful engineering practices."
            )

        elif status == "declined":

            return (
                "Repository health is declining and "
                "technical debt may be increasing."
            )

        return (
            "Repository health remains stable."
        )

    # ---------------------------------------------

    def _execution_reasoning(self):

        execution = self.report.get("execution", {})

        status = execution.get("status", "stable")

        if status == "expanded":

            return (
                "Execution graph continues to expand, "
                "suggesting repository capabilities are growing."
            )

        elif status == "reduced":

            return (
                "Execution graph has become smaller, "
                "likely due to simplification or refactoring."
            )

        return (
            "Execution architecture remains stable."
        )

    # ---------------------------------------------

    def _knowledge_reasoning(self):

        knowledge = self.report.get("knowledge", {})

        dead = knowledge.get("dead_code", {}).get("delta", 0)

        hotspots = knowledge.get("hotspots", {}).get("delta", 0)

        observations = []

        if dead < 0:

            observations.append(
                "Technical debt is decreasing."
            )

        elif dead > 0:

            observations.append(
                "Technical debt is increasing."
            )

        if hotspots < 0:

            observations.append(
                "Repository hotspots are becoming more stable."
            )

        elif hotspots > 0:

            observations.append(
                "Repository hotspots continue to grow."
            )

        if not observations:

            observations.append(
                "Repository knowledge structure remains stable."
            )

        return " ".join(observations)

    # ---------------------------------------------

    def _engineering_direction(self):

        health_status = self.report.get(
            "health", {}
        ).get(
            "status", "unchanged"
        )

        execution_status = self.report.get(
            "execution", {}
        ).get(
            "status", "stable"
        )

        if health_status == "improved" and execution_status == "expanded":

            return (
                "Engineering effort is improving quality while "
                "expanding repository capabilities."
            )

        if health_status == "improved":

            return (
                "Engineering effort is focused on repository quality."
            )

        if execution_status == "expanded":

            return (
                "Engineering effort is focused on feature growth."
            )

        return (
            "Engineering direction appears stable."
        )

    # ---------------------------------------------

    def _repository_momentum(self):

        health = self.report.get(
            "health", {}
        ).get(
            "status", "unchanged"
        )

        if health == "improved":

            return "Positive"

        elif health == "declined":

            return "Negative"

        return "Stable"

    # ---------------------------------------------

    def build(self):

        reasoning = {

            "health_reasoning":
                self._health_reasoning(),

            "execution_reasoning":
                self._execution_reasoning(),

            "knowledge_reasoning":
                self._knowledge_reasoning(),

            "engineering_direction":
                self._engineering_direction(),

            "repository_momentum":
                self._repository_momentum()

        }

        return reasoning