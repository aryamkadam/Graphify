"""
Graphify

Phase 5

Stage P5.3

Repository Learning Engine

Learns engineering patterns from
multiple completed repository evolutions.

Author:
Graphify Core
"""


class RepositoryLearningEngine:

    VERSION = "P5.3"

    # --------------------------------------------------

    def build(self, history):

        if not history:

            return {
                "patterns": [],
                "summary": "No repository history available.",
                "version": self.VERSION,
            }

        total_health = 0
        total_execution = 0
        total_dead = 0
        total_hotspots = 0

        for sprint in history:

            total_health += sprint.get(
                "health", {}
            ).get(
                "delta", 0
            )

            total_execution += sprint.get(
                "execution", {}
            ).get(
                "delta", 0
            )

            total_dead += sprint.get(
                "knowledge", {}
            ).get(
                "dead_code", {}
            ).get(
                "delta", 0
            )

            total_hotspots += sprint.get(
                "knowledge", {}
            ).get(
                "hotspots", {}
            ).get(
                "delta", 0
            )

        patterns = []

        # ------------------------

        if total_health > 0:

            patterns.append(
                "Repository health consistently improves."
            )

        elif total_health < 0:

            patterns.append(
                "Repository health consistently declines."
            )

        # ------------------------

        if total_execution > 0:

            patterns.append(
                "Repository capabilities continue expanding."
            )

        elif total_execution < 0:

            patterns.append(
                "Repository execution graph is shrinking."
            )

        # ------------------------

        if total_dead < 0:

            patterns.append(
                "Technical debt consistently decreases."
            )

        elif total_dead > 0:

            patterns.append(
                "Technical debt continues growing."
            )

        # ------------------------

        if total_hotspots < 0:

            patterns.append(
                "Repository hotspots are becoming more stable."
            )

        elif total_hotspots > 0:

            patterns.append(
                "Repository hotspots continue growing."
            )

        # ------------------------

        summary = (
            f"Learned {len(patterns)} engineering patterns "
            f"from {len(history)} completed repository evolutions."
        )

        return {

            "patterns": patterns,

            "summary": summary,

            "version": self.VERSION,

        }