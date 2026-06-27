"""
Stage 15.9.1

Repository Trend Analyzer

Analyzes repository metrics and determines
whether they are improving, stable,
or degrading.

This becomes the foundation for
future prediction.
"""


class RepositoryTrendAnalyzer:

    def analyze(self, repository_brain):

        health = repository_brain["health"]
        knowledge = repository_brain["knowledge"]
        execution = repository_brain["execution"]

        trends = {}

        # -------------------------
        # Health Trend
        # -------------------------

        score = health["health_score"]

        if score >= 90:
            trends["health"] = "Improving"

        elif score >= 75:
            trends["health"] = "Stable"

        else:
            trends["health"] = "Declining"

        # -------------------------
        # Dead Code Trend
        # -------------------------

        dead = knowledge["dead_code_count"]

        if dead == 0:
            trends["dead_code"] = "Clean"

        elif dead < 20:
            trends["dead_code"] = "Growing"

        else:
            trends["dead_code"] = "Critical"

        # -------------------------
        # Hotspots
        # -------------------------

        hotspots = knowledge["hotspot_count"]

        if hotspots < 5:
            trends["hotspots"] = "Stable"

        elif hotspots < 15:
            trends["hotspots"] = "Increasing"

        else:
            trends["hotspots"] = "High Risk"

        # -------------------------
        # Execution Complexity
        # -------------------------

        nodes = execution["graph_nodes"]

        if nodes < 150:
            trends["execution"] = "Simple"

        elif nodes < 300:
            trends["execution"] = "Growing"

        else:
            trends["execution"] = "Complex"

        # -------------------------

        return {

            "health_score": score,

            "graph_nodes": nodes,

            "dead_code": dead,

            "hotspots": hotspots,

            "trends": trends

        }