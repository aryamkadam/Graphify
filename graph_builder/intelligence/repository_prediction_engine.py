"""
Stage 15.9.2

Repository Prediction Engine

Uses current repository trends to forecast
future repository health and engineering risk.

Future versions will use historical commits
and machine learning.

Current version uses deterministic reasoning.
"""


class RepositoryPredictionEngine:

    def predict(self, trend_report):

        health = trend_report["health_score"]
        dead = trend_report["dead_code"]
        hotspots = trend_report["hotspots"]
        nodes = trend_report["graph_nodes"]

        predicted_health = health

        predictions = []

        confidence = 0.80

        # ----------------------------
        # Dead Code
        # ----------------------------

        if dead > 0:

            predicted_health -= 3

            predictions.append(
                "Dead code is expected to increase if not removed."
            )

        # ----------------------------
        # Hotspots
        # ----------------------------

        if hotspots >= 5:

            predicted_health -= 4

            predictions.append(
                "Hotspot files will continue changing frequently."
            )

        # ----------------------------
        # Execution Complexity
        # ----------------------------

        if nodes >= 300:

            predicted_health -= 5

            predictions.append(
                "Execution complexity is likely to increase."
            )

        elif nodes >= 150:

            predicted_health -= 2

            predictions.append(
                "Execution graph is gradually expanding."
            )

        # ----------------------------
        # Clamp health
        # ----------------------------

        if predicted_health < 0:
            predicted_health = 0

        if predicted_health > 100:
            predicted_health = 100

        # ----------------------------
        # Risk Level
        # ----------------------------

        if predicted_health >= 90:
            risk = "Low"

        elif predicted_health >= 75:
            risk = "Medium"

        elif predicted_health >= 60:
            risk = "High"

        else:
            risk = "Critical"

        return {

            "predicted_health": predicted_health,

            "risk_level": risk,

            "confidence": confidence,

            "predictions": predictions

        }