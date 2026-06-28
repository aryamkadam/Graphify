"""
Stage 15.6

Repository Consciousness Engine

Builds the high-level identity of the repository.

Consumes the NEW Repository Brain structure.
"""


class RepositoryConsciousnessEngine:

    def __init__(self, intelligence):

        self.intelligence = intelligence

    # ------------------------------------------------

    def _identity(self):

        metadata = self.intelligence.get("metadata", {})

        return {

            "repository": metadata.get(
                "repository_name",
                "Unknown"
            ),

            "branch": metadata.get(
                "current_branch",
                "unknown"
            ),

            "latest_commit": metadata.get(
                "latest_commit",
                "unknown"
            )

        }

    # ------------------------------------------------

    def _mission(self):

        insights = self.intelligence.get(
            "insights",
            {}
        )

        area = insights.get(
            "dominant_area",
            "software evolution"
        )

        return (

            f"Repository is primarily focused on "

            f"{area}."

        )

    # ------------------------------------------------

    def _strengths(self):

        strengths = []

        health = self.intelligence.get(
            "health",
            {}
        )

        knowledge = self.intelligence.get(
            "knowledge",
            {}
        )

        execution = self.intelligence.get(
            "execution",
            {}
        )

        if health.get(
            "health_score",
            0
        ) >= 90:

            strengths.append(
                "Healthy architecture"
            )

        if knowledge.get(
            "critical_symbols",
            []
        ):

            strengths.append(
                "Clear critical modules"
            )

        if execution.get(
            "top_important_functions",
            []
        ):

            strengths.append(
                "Execution flow understood"
            )

        return strengths

    # ------------------------------------------------

    def _weaknesses(self):

        weaknesses = []

        knowledge = self.intelligence.get(
            "knowledge",
            {}
        )

        if knowledge.get(
            "dead_code_count",
            0
        ) > 0:

            weaknesses.append(
                "Dead code exists"
            )

        if knowledge.get(
            "risky_symbols",
            []
        ):

            weaknesses.append(
                "High-risk symbols detected"
            )

        return weaknesses

    # ------------------------------------------------

    def _goal(self):

        score = self.intelligence.get(
            "health",
            {}
        ).get(
            "health_score",
            0
        )

        if score >= 90:

            return (
                "Scale into an enterprise-grade repository."
            )

        elif score >= 70:

            return (
                "Continue improving architecture."
            )

        return (
            "Stabilize the repository before expansion."
        )

    # ------------------------------------------------

    def _evolution(self):

        commits = self.intelligence.get(
            "metadata",
            {}
        ).get(
            "total_commits",
            0
        )

        if commits < 20:

            return "Emerging"

        elif commits < 100:

            return "Growing"

        elif commits < 300:

            return "Maturing"

        return "Enterprise"

    # ------------------------------------------------

    def build(self):

        return {

            "identity":
                self._identity(),

            "mission":
                self._mission(),

            "strengths":
                self._strengths(),

            "weaknesses":
                self._weaknesses(),

            "goal":
                self._goal(),

            "evolution_stage":
                self._evolution()

        }