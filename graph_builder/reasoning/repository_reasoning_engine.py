"""
Stage 15.4

Repository Reasoning Engine

Converts Repository Intelligence
into human-like understanding.

This is the first reasoning layer
of Graphify.

Future versions will use LLMs.

Current version uses deterministic
reasoning rules.
"""


class RepositoryReasoningEngine:

    def __init__(self, intelligence):

        self.intelligence = intelligence

    # -------------------------------------------------

    def _repository_purpose(self):

        health = self.intelligence["health"]

        score = health["health_score"]

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

        insights = self.intelligence["decisions"]["insights"]

        return insights.get(

            "dominant_area",

            "Unknown"

        )

    # -------------------------------------------------

    def _biggest_risk(self):

        knowledge = self.intelligence["knowledge"]

        if knowledge["dead_code"]:

            return "Dead code accumulation"

        if knowledge["risky_symbols"]:

            return "High-risk symbols detected"

        return "No major repository risks detected"

    # -------------------------------------------------

    def _critical_module(self):

        knowledge = self.intelligence["knowledge"]

        if not knowledge["critical_symbols"]:

            return "Unknown"

        return knowledge["critical_symbols"][0]["symbol"]

    # -------------------------------------------------

    def _recommended_next_step(self):

        recommendations = self.intelligence["health"][

            "top_recommendations"

        ]

        if recommendations:

            return recommendations[0]

        return "Continue repository evolution"

    # -------------------------------------------------

    def _repository_story(self):

        metadata = self.intelligence["identity"]

        commits = metadata["total_commits"]

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