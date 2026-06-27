"""
Stage 15.7.1

Repository Reasoning Rules

This module contains the core reasoning
rules used by Graphify.

Every future AI engine should reason using
these rules instead of hardcoded logic.

These rules become the "thinking layer"
of Graphify.
"""


class RepositoryReasoningRules:

    """
    Repository reasoning rule engine.

    Converts repository metrics into
    human-like reasoning.
    """

    # -------------------------------------

    def analyze_health(
        self,
        health_report,
    ):

        score = health_report["health_score"]

        reasons = []

        if score >= 90:

            reasons.append(
                "Repository is highly stable."
            )

        elif score >= 75:

            reasons.append(
                "Repository is generally healthy but requires monitoring."
            )

        elif score >= 60:

            reasons.append(
                "Repository health is degrading."
            )

        else:

            reasons.append(
                "Repository requires immediate stabilization."
            )

        if health_report["dead_code"] > 0:

            reasons.append(
                "Dead code is reducing maintainability."
            )

        if health_report["god_files"] > 0:

            reasons.append(
                "God files increase architectural complexity."
            )

        if len(
            health_report["high_risk_symbols"]
        ) > 0:

            reasons.append(
                "Critical symbols introduce maintenance risk."
            )

        return reasons

    # -------------------------------------

    def analyze_execution(
        self,
        execution_engine,
    ):

        stats = execution_engine["statistics"]

        reasons = []

        if stats["graph_nodes"] > 500:

            reasons.append(
                "Execution graph is becoming large."
            )

        if stats["execution_paths"] > 300:

            reasons.append(
                "Execution complexity is increasing."
            )

        if stats["reverse_call_entries"] > 200:

            reasons.append(
                "Function coupling is growing."
            )

        return reasons

    # -------------------------------------

    def analyze_knowledge(
        self,
        knowledge,
    ):

        reasons = []

        if knowledge["dead_code_count"] > 0:

            reasons.append(
                "Repository contains unused implementation."
            )

        if knowledge["hotspot_count"] > 5:

            reasons.append(
                "Several files change frequently."
            )

        if len(
            knowledge["critical_symbols"]
        ) > 0:

            reasons.append(
                "Critical modules should receive additional testing."
            )

        return reasons

    # -------------------------------------

    def analyze_decisions(
        self,
        decisions,
    ):

        reasons = []

        if decisions["decision_count"] == 0:

            reasons.append(
                "Project lacks documented decisions."
            )

        elif decisions["decision_count"] < 10:

            reasons.append(
                "Decision history is still growing."
            )

        else:

            reasons.append(
                "Repository preserves architectural knowledge."
            )

        return reasons

    # -------------------------------------

    def analyze_repository_direction(
        self,
        insights,
    ):

        reasons = []

        reasons.append(

            f"Current development direction focuses on "

            f"{insights['dominant_area']}."

        )

        return reasons