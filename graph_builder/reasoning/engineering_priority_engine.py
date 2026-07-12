"""
Graphify

Stage 39.0

Engineering Priority Engine

Author:
Graphify Core
"""


class EngineeringPriorityEngine:

    VERSION = "39.0"

    PRIORITY_TABLE = {
        "HIGH": 100,
        "MEDIUM": 60,
        "LOW": 20,
    }

    def prioritize(self, recommendations):

        ranked = []

        for item in recommendations:

            score = self.PRIORITY_TABLE.get(
                item.get("severity", "LOW"),
                0,
            )

            ranked.append(
                {
                    **item,
                    "priority_score": score,
                }
            )

        ranked.sort(
            key=lambda x: x["priority_score"],
            reverse=True,
        )

        return ranked