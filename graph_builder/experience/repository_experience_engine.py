"""
Stage 17.8

Repository Experience Engine

Transforms repository memory and reasoning
into accumulated engineering experience.

Experience is different from memory.

Memory remembers events.

Experience remembers what repeatedly works.

Future Repository Brain modules will use this
experience to make architectural decisions.
"""


class RepositoryExperienceEngine:

    def build(

        self,

        memory_reasoning,

    ):

        experiences = self._build_experience(

            memory_reasoning,

        )

        instincts = self._build_instincts(

            experiences,

        )

        bias = self._build_bias(

            experiences,

        )

        level = self._experience_level(

            experiences,

        )

        wisdom = self._repository_wisdom(

            experiences,

        )

        return {

            "engineering_experience": experiences,

            "repository_instincts": instincts,

            "future_engineering_bias": bias,

            "experience_level": level,

            "repository_wisdom": wisdom,

        }

    # ---------------------------------------------

    def _build_experience(

        self,

        reasoning,

    ):

        experiences = []

        lessons = reasoning.get(

            "engineering_experience",

            [],

        )

        for lesson in lessons:

            experiences.append(

                {

                    "experience": lesson["experience"],

                    "confidence": lesson["confidence"],

                    "impact": lesson["impact"],

                    "evidence": 1,

                }

            )

        return experiences

    # ---------------------------------------------

    def _build_instincts(

        self,

        experiences,

    ):

        instincts = []

        for exp in experiences:

            instincts.append(

                "Prefer engineering practices that previously improved repository health."

            )

        return instincts

    # ---------------------------------------------

    def _build_bias(

        self,

        experiences,

    ):

        if not experiences:

            return []

        return [

            "Favor refactoring before feature expansion.",

            "Reduce technical debt whenever possible.",

        ]

    # ---------------------------------------------

    def _experience_level(

        self,

        experiences,

    ):

        count = len(experiences)

        if count == 0:
            return "Learning"

        elif count < 3:
            return "Junior"

        elif count < 6:
            return "Intermediate"

        elif count < 10:
            return "Senior"

        elif count < 20:
            return "Principal"

        return "Repository Architect"

    # ---------------------------------------------

    def _repository_wisdom(

        self,

        experiences,

    ):

        if not experiences:

            return (

                "Repository experience is still forming."

            )

        return (

            "Repository experience suggests that "
            "systematic refactoring and technical "
            "debt reduction consistently improve "
            "repository quality."

        )