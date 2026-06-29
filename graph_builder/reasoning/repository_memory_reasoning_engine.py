"""
Stage 17.7

Repository Memory Reasoning Engine

Uses Repository Evolution Memory to build
high-level engineering understanding.

This is the first component where Graphify
starts reasoning from experience instead of
individual repository snapshots.
"""


class RepositoryMemoryReasoningEngine:

    def build(

        self,

        evolution_memory,

    ):

        identity = evolution_memory.get(

            "repository_identity",

            {},

        )

        patterns = evolution_memory.get(

            "engineering_patterns",

            {},

        )

        lessons = evolution_memory.get(

            "long_term_lessons",

            [],

        )

        decision_history = evolution_memory.get(

            "decision_history",

            [],

        )

        repository_understanding = (

            self._repository_understanding(

                identity,

                patterns,

            )

        )

        engineering_experience = (

            self._engineering_experience(

                lessons,

            )

        )

        recommendation = (

            self._future_recommendation(

                patterns,

            )

        )

        confidence = (

            self._confidence(

                lessons,

            )

        )

        brain_state = (

            self._brain_state(

                lessons,

            )

        )

        return {

            "repository_understanding":

                repository_understanding,

            "engineering_experience":

                engineering_experience,

            "recommended_future_decision":

                recommendation,

            "reasoning_confidence":

                confidence,

            "brain_state":

                brain_state,

            "known_decisions":

                len(decision_history),

        }

    # ------------------------------------------

    def _repository_understanding(

        self,

        identity,

        patterns,

    ):

        return (

            f"The repository is currently in the "

            f"{identity.get('phase','Unknown')} phase. "

            f"Engineering direction is "

            f"{identity.get('technical_direction','Unknown')} "

            f"while repository health trend is "

            f"{patterns.get('health_trend','Unknown')}."

        )

    # ------------------------------------------

    def _engineering_experience(

        self,

        lessons,

    ):

        experience = []

        for lesson in lessons:

            experience.append(

                {

                    "experience":

                        lesson["lesson"],

                    "confidence":

                        lesson["confidence"],

                    "impact":

                        lesson["impact"],

                }

            )

        return experience

    # ------------------------------------------

    def _future_recommendation(

        self,

        patterns,

    ):

        if (

            patterns.get(

                "technical_debt"

            )

            ==

            "decreasing"

        ):

            return (

                "Continue repository-wide "

                "refactoring and technical "

                "debt reduction."

            )

        return (

            "Continue monitoring repository "

            "engineering trends."

        )

    # ------------------------------------------

    def _confidence(

        self,

        lessons,

    ):

        if not lessons:

            return 0.50

        values = [

            lesson["confidence"]

            for lesson in lessons

        ]

        return round(

            sum(values) / len(values),

            2,

        )

    # ------------------------------------------

    def _brain_state(

        self,

        lessons,

    ):

        count = len(lessons)

        if count == 0:
            return "Learning"

        if count < 5:
            return "Growing"

        if count < 10:
            return "Experienced"

        if count < 20:
            return "Expert"

        return "Architect"