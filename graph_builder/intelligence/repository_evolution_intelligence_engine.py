"""
Stage 17.4

Repository Evolution Intelligence Engine

Converts repository history into high-level
engineering intelligence.

This is the first module that behaves like
a Senior Software Architect instead of a
report generator.
"""


class RepositoryEvolutionIntelligenceEngine:

    def build(

        self,

        timeline,

        learning,

        decision_graph,

    ):

        patterns = learning.get("patterns", {})
        decisions = decision_graph.get(
            "decision_graph",
            []
        )

        repository_phase = self._phase(patterns)

        velocity = self._velocity(patterns)

        direction = self._direction(patterns)

        risk = self._risk(patterns)

        confidence = self._confidence(patterns)

        intelligence = self._summary(

            repository_phase,

            velocity,

            direction,

            risk,

            patterns,

        )

        return {

            "repository_phase": repository_phase,

            "engineering_velocity": velocity,

            "technical_direction": direction,

            "future_risk": risk,

            "architectural_confidence": confidence,

            "overall_intelligence": intelligence,

            "decision_count": len(decisions),

        }

    # ----------------------------------------

    def _phase(self, patterns):

        health = patterns.get("health_trend")
        debt = patterns.get("technical_debt")

        if health == "improving" and debt == "decreasing":
            return "Stabilization"

        if health == "improving":
            return "Growth"

        if health == "declining":
            return "Critical"

        return "Maintenance"

    # ----------------------------------------

    def _velocity(self, patterns):

        execution = patterns.get("execution_growth")

        if execution == "expanding":
            return "Healthy"

        if execution == "declining":
            return "Slow"

        return "Stable"

    # ----------------------------------------

    def _direction(self, patterns):

        return {

            "improving": "Positive",

            "declining": "Negative",

            "stable": "Neutral"

        }.get(

            patterns.get("health_trend"),

            "Neutral"

        )

    # ----------------------------------------

    def _risk(self, patterns):

        debt = patterns.get("technical_debt")
        architecture = patterns.get("architecture_trend")

        if debt == "increasing":
            return "High"

        if architecture == "decreasing":
            return "Medium"

        return "Low"

    # ----------------------------------------

    def _confidence(self, patterns):

        score = 1.0

        if patterns.get("health_trend") == "stable":
            score -= 0.05

        if patterns.get("execution_growth") == "stable":
            score -= 0.03

        if patterns.get("technical_debt") == "stable":
            score -= 0.02

        return round(score, 2)

    # ----------------------------------------

    def _summary(

        self,

        phase,

        velocity,

        direction,

        risk,

        patterns,

    ):

        return (

            f"Repository is currently in the "

            f"{phase} phase. "

            f"Engineering velocity is {velocity.lower()}. "

            f"Overall direction remains {direction.lower()}. "

            f"Future engineering risk is {risk.lower()}. "

            f"Health trend is "

            f"{patterns.get('health_trend')}, "

            f"technical debt is "

            f"{patterns.get('technical_debt')}, "

            f"and architecture trend is "

            f"{patterns.get('architecture_trend')}."

        )