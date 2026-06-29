"""
Stage 17.6

Repository Evolution Memory Engine

Creates a permanent engineering memory from the
entire repository evolution pipeline.

This memory becomes the long-term Repository Brain
used by AI exports and future reasoning.
"""


class RepositoryEvolutionMemoryEngine:

    def build(

        self,

        timeline,

        learning,

        explanations,

        cause_effect,

        decision_graph,

        intelligence,

        story,

    ):

        memory = {

            "memory_version": "17.6",

            "repository_identity": {

                "phase":
                    intelligence.get(
                        "repository_phase"
                    ),

                "technical_direction":
                    intelligence.get(
                        "technical_direction"
                    ),

                "engineering_velocity":
                    intelligence.get(
                        "engineering_velocity"
                    ),

                "future_risk":
                    intelligence.get(
                        "future_risk"
                    ),

            },

            "timeline_summary":
                timeline.get(
                    "timeline_summary"
                ),
            "engineering_story": {

                "past":
                    story.get("past"),

                "present":
                    story.get("present"),

                "future":
                    story.get("future"),

                "summary":
                    story.get("summary"),

            },

            "decision_history":
                decision_graph.get(
                    "decision_graph",
                    [],
                ),

            "engineering_patterns":
                learning.get(
                    "patterns",
                    {},
                ),

            "long_term_lessons":
                self._extract_lessons(
                    decision_graph
                ),

            "repository_memory_strength":
                self._memory_strength(
                    decision_graph
                ),

            "repository_experience":
                self._summary(
                    decision_graph
                ),

        }

        return memory

    # --------------------------------------------

    def _extract_lessons(
        self,
        decision_graph,
    ):

        lessons = []

        for decision in decision_graph.get(
            "decision_graph",
            [],
        ):

            lessons.append({

                "decision":
                    decision.get(
                        "decision"
                    ),

                "lesson":

                    "This engineering decision should "
                    "be remembered for future repository "
                    "improvements.",

                "confidence":
                    decision.get(
                        "confidence",
                        0,
                    ),

                "impact":
                    decision.get(
                        "impact",
                        "Unknown",
                    ),

            })

        return lessons

    # --------------------------------------------

    def _memory_strength(
        self,
        decision_graph,
    ):

        decisions = len(

            decision_graph.get(
                "decision_graph",
                [],
            )

        )

        if decisions == 0:
            return 0.0

        strength = min(
            1.0,
            0.5 + decisions * 0.1,
        )

        return round(
            strength,
            2,
        )

    # --------------------------------------------

    def _summary(
        self,
        decision_graph,
    ):

        count = len(

            decision_graph.get(
                "decision_graph",
                [],
            )

        )

        return (

            f"Graphify currently remembers "

            f"{count} engineering decisions."

        )