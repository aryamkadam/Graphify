"""
Stage 16.5

Repository Evolution Story Engine

Transforms repository evolution into a
human-readable engineering story.

This becomes the historical memory
used by future AI reasoning.
"""


class RepositoryEvolutionStoryEngine:

    def build(self, evolution, reasoning):

        story = {

            "past": self._past(evolution),

            "present": self._present(reasoning),

            "future": self._future(reasoning),

            "summary": self._summary(

                evolution,

                reasoning

            )

        }

        return story

    # ---------------------------------------------

    def _past(self, evolution):

        health = evolution["health"]

        if health["delta"] > 0:

            return (

                "The repository has recently become healthier."

            )

        elif health["delta"] < 0:

            return (

                "Repository quality has recently declined."

            )

        return (

            "Repository health remained stable."

        )

    # ---------------------------------------------

    def _present(self, reasoning):

        return (

            reasoning["engineering_direction"]

        )

    # ---------------------------------------------

    def _future(self, reasoning):

        momentum = reasoning["repository_momentum"]

        if momentum == "Positive":

            return (

                "If current practices continue, "

                "the repository is expected to mature "

                "into a highly maintainable system."

            )

        if momentum == "Negative":

            return (

                "Current engineering trends may "

                "introduce long-term technical debt."

            )

        return (

            "Repository is expected to remain stable."

        )

    # ---------------------------------------------

    def _summary(

        self,

        evolution,

        reasoning

    ):

        return (

            f"{evolution['summary']} "

            f"{reasoning['engineering_direction']}"

        )