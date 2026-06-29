"""
Stage 17.9

Repository Knowledge Engine

Transforms engineering experience into
persistent repository knowledge.

Experience answers:

"What usually works?"

Knowledge answers:

"What is objectively true about this repository?"

Knowledge becomes permanent Repository Brain
knowledge and can be exported across AI systems.
"""


class RepositoryKnowledgeEngine:

    def build(

        self,

        experience,

    ):

        principles = self._engineering_principles(

            experience,

        )

        best_practices = self._best_practices(

            experience,

        )

        repository_rules = self._repository_rules(

            experience,

        )

        confidence = self._knowledge_confidence(

            principles,

        )

        summary = self._knowledge_summary(

            principles,

            confidence,

        )

        return {

            "engineering_principles": principles,

            "best_practices": best_practices,

            "repository_rules": repository_rules,

            "knowledge_confidence": confidence,

            "repository_knowledge": summary,

        }

    # ---------------------------------------------

    def _engineering_principles(

        self,

        experience,

    ):

        principles = []

        for exp in experience.get(

            "engineering_experience",

            [],

        ):

            principles.append(

                {

                    "principle":

                        "Continuous refactoring improves long-term repository quality.",

                    "confidence":

                        exp["confidence"],

                    "source":

                        exp["experience"],

                }

            )

        return principles

    # ---------------------------------------------

    def _best_practices(

        self,

        experience,

    ):

        return [

            "Reduce technical debt continuously.",

            "Refactor before adding major features.",

            "Stabilize architectural hotspots early.",

            "Prefer maintainability over complexity.",

        ]

    # ---------------------------------------------

    def _repository_rules(

        self,

        experience,

    ):

        return [

            "Repository health should never decrease after major changes.",

            "Execution growth should remain understandable.",

            "Architectural complexity must stay controlled.",

        ]

    # ---------------------------------------------

    def _knowledge_confidence(

        self,

        principles,

    ):

        if not principles:

            return 0.0

        return round(

            sum(

                p["confidence"]

                for p in principles

            )

            / len(principles),

            2,

        )

    # ---------------------------------------------

    def _knowledge_summary(

        self,

        principles,

        confidence,

    ):

        if not principles:

            return (

                "Repository knowledge has not formed yet."

            )

        return (

            "Repository knowledge indicates that "
            "systematic engineering discipline, "
            "continuous refactoring, and technical "
            "debt reduction consistently produce "
            "higher repository quality."

        )