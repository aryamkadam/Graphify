"""
Stage 15.4

Repository Reasoning Engine

Converts Repository Intelligence
into human-like understanding.

Compatible with the NEW Repository Brain.
"""


class RepositoryReasoningEngine:

    def __init__(self, intelligence):

        self.intelligence = intelligence

    # -------------------------------------------------

    def _repository_purpose(self):

        health = self.intelligence.get(
            "health",
            {}
        )

        score = health.get(
            "health_score",
            0
        )

        if score >= 90:

            return (
                "Repository is mature and actively maintained."
            )

        elif score >= 75:

            return (
                "Repository is under active development."
            )

        elif score >= 50:

            return (
                "Repository is evolving but requires improvements."
            )

        return (
            "Repository needs major architectural attention."
        )

    # -------------------------------------------------

    def _current_focus(self):

        insights = self.intelligence.get(
            "insights",
            {}
        )

        return insights.get(
            "dominant_area",
            "Unknown"
        )

    # -------------------------------------------------

    def _biggest_risk(self):

        knowledge = self.intelligence.get(
            "knowledge",
            {}
        )

        if knowledge.get(
            "dead_code_count",
            0
        ) > 0:

            return "Dead code accumulation"

        if knowledge.get(
            "risky_symbols",
            []
        ):

            return "High-risk symbols detected"

        return "No major repository risks detected"

    # -------------------------------------------------

    def _critical_module(self):

        knowledge = self.intelligence.get(
            "knowledge",
            {}
        )

        critical = knowledge.get(
            "critical_symbols",
            []
        )

        if not critical:

            return "Unknown"

        first = critical[0]

        if isinstance(first, dict):

            return first.get(
                "symbol",
                "Unknown"
            )

        return str(first)

    # -------------------------------------------------

    def _recommended_next_step(self):

        recommendations = self.intelligence.get(
            "health",
            {}
        ).get(
            "top_recommendations",
            []
        )

        if recommendations:

            return recommendations[0]

        return "Continue repository evolution"

    # -------------------------------------------------

    def _repository_story(self):

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
                "Repository is in an early growth phase."
            )

        elif commits < 100:

            return (
                "Repository is steadily evolving."
            )

        elif commits < 500:

            return (
                "Repository has become a mature software project."
            )

        return (
            "Repository has a long development history."
        )

    # -------------------------------------------------

    def build(self):

        reasoning = {

            "repository_purpose":
                self._repository_purpose(),

            "current_focus":
                self._current_focus(),

            "biggest_risk":
                self._biggest_risk(),

            "critical_module":
                self._critical_module(),

            "recommended_next_step":
                self._recommended_next_step(),

            "repository_story":
                self._repository_story(),

        }

        return reasoning