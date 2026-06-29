"""
Stage 17.2

Repository Change Explanation Engine

Explains WHY repository evolution happened.

Timeline tells us WHAT changed.

Explanation tells us WHY it changed.

Future AI agents will use these explanations
instead of raw numerical changes.
"""


class RepositoryChangeExplanationEngine:

    def build(

        self,

        timeline,

        evolution_reports,

        learning,

    ):

        explanations = []

        events = timeline.get("events", [])

        reports = evolution_reports

        patterns = learning.get(
            "patterns",
            {}
        )

        for index in range(1, len(events)):

            previous = events[index - 1]
            current = events[index]

            report = reports[index - 1]

            explanations.append(

                self._explain_change(

                    previous,

                    current,

                    report,

                    patterns,

                )

            )

        return {

            "explanations": explanations,

            "summary": self._summary(explanations)

        }

    # ------------------------------------------------

    def _explain_change(

        self,

        previous,

        current,

        report,

        patterns,

    ):

        reasons = []

        health = report["health"]["delta"]

        execution = report["execution"]["delta"]

        dead = report["knowledge"]["dead_code"]["delta"]

        hotspots = report["knowledge"]["hotspots"]["delta"]

        if health > 0:

            reasons.append(

                "repository health improved"

            )

        elif health < 0:

            reasons.append(

                "repository health declined"

            )

        if dead < 0:

            reasons.append(

                "technical debt decreased"

            )

        elif dead > 0:

            reasons.append(

                "technical debt increased"

            )

        if hotspots < 0:

            reasons.append(

                "hotspots became more stable"

            )

        elif hotspots > 0:

            reasons.append(

                "more architectural hotspots appeared"

            )

        if execution > 0:

            reasons.append(

                "execution capabilities expanded"

            )

        elif execution < 0:

            reasons.append(

                "execution complexity reduced"

            )

        explanation = {

            "from": previous["timestamp"],

            "to": current["timestamp"],

            "change": current["change"],

            "because": reasons,

            "overall_direction": current["direction"],

            "engineering_pattern": {

    "health": patterns.get(
        "health_trend",
        "unknown"
    ),

    "execution": patterns.get(
        "execution_growth",
        "unknown"
    ),

    "technical_debt": patterns.get(
        "technical_debt",
        "unknown"
    ),

    "architecture": patterns.get(
        "architecture_trend",
        "unknown"
    )

}

        }

        return explanation

    # ------------------------------------------------

    def _summary(

        self,

        explanations,

    ):

        if not explanations:

            return (

                "No repository evolution detected."

            )

        return (

            f"{len(explanations)} repository "

            f"changes successfully explained."

        )