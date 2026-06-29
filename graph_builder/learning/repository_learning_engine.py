"""
Stage 16.6

Repository Learning Engine

Learns long-term engineering patterns
from multiple repository evolution reports.

This transforms repository history into
engineering knowledge.

Future AI agents consume this learning
instead of raw repository history.
"""


class RepositoryLearningEngine:

    def build(self, evolution_history):

        if not evolution_history:

            return {

                "learning_summary": [],

                "patterns": {},

                "repository_learning": {}

            }

        health_deltas = []
        execution_deltas = []
        dead_code_deltas = []
        hotspot_deltas = []

        for report in evolution_history:

            health_deltas.append(
                report["health"]["delta"]
            )

            execution_deltas.append(
                report["execution"]["delta"]
            )

            dead_code_deltas.append(
                report["knowledge"]["dead_code"]["delta"]
            )

            hotspot_deltas.append(
                report["knowledge"]["hotspots"]["delta"]
            )

        patterns = {

            "health_trend":
                self._health_trend(health_deltas),

            "execution_growth":
                self._execution_trend(execution_deltas),

            "technical_debt":
                self._technical_debt_trend(dead_code_deltas),

            "architecture_stability":
                self._architecture_stability(hotspot_deltas)

        }

        summary = self._build_summary(patterns)

        learning = {

            "confidence":
                self._confidence(len(evolution_history)),

            "engineering_maturity":
                self._engineering_maturity(patterns),

            "long_term_direction":
                self._direction(patterns)

        }

        return {

            "learning_summary": summary,

            "patterns": patterns,

            "repository_learning": learning

        }

    # ----------------------------------------------------
    # Domain-specific reasoning methods
    # ----------------------------------------------------

    def _health_trend(self, values):

        total = sum(values)

        if total > 0:
            return "improving"

        if total < 0:
            return "declining"

        return "stable"

    # ----------------------------------------------------

    def _execution_trend(self, values):

        total = sum(values)

        if total > 0:
            return "expanding"

        if total < 0:
            return "shrinking"

        return "stable"

    # ----------------------------------------------------

    def _technical_debt_trend(self, values):

        total = sum(values)

        if total < 0:
            return "decreasing"

        if total > 0:
            return "increasing"

        return "stable"

    # ----------------------------------------------------

    def _architecture_stability(self, values):

        total = sum(values)

        # Hotspots decreasing
        # =>
        # Stability increasing

        if total < 0:
            return "increasing"

        # Hotspots increasing
        # =>
        # Stability decreasing

        if total > 0:
            return "decreasing"

        return "stable"

    # ----------------------------------------------------

    def _build_summary(self, patterns):

        summary = []

        summary.append(

            f"Repository health is {patterns['health_trend']}."

        )

        summary.append(

            f"Execution complexity is {patterns['execution_growth']}."

        )

        summary.append(

            f"Technical debt is {patterns['technical_debt']}."

        )

        summary.append(

            f"Architecture stability is {patterns['architecture_stability']}."

        )

        return summary

    # ----------------------------------------------------

    def _confidence(self, snapshots):

        if snapshots >= 20:
            return 0.98

        if snapshots >= 10:
            return 0.95

        if snapshots >= 5:
            return 0.90

        return 0.80

    # ----------------------------------------------------

    def _engineering_maturity(self, patterns):

        if (

            patterns["health_trend"] == "improving"

            and

            patterns["technical_debt"] == "decreasing"

            and

            patterns["architecture_stability"] == "increasing"

        ):

            return "Growing"

        elif (

            patterns["health_trend"] == "stable"

            and

            patterns["technical_debt"] == "stable"

        ):

            return "Stable"

        return "Needs Attention"

    # ----------------------------------------------------

    def _direction(self, patterns):

        score = 0

        if patterns["health_trend"] == "improving":
            score += 1

        if patterns["technical_debt"] == "decreasing":
            score += 1

        if patterns["architecture_stability"] == "increasing":
            score += 1

        if patterns["execution_growth"] == "expanding":
            score += 1

        if score >= 3:
            return "Positive"

        if score <= 1:
            return "Negative"

        return "Neutral"