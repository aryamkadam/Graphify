"""
Stage 18.5

Repository Executive Brain

Unifies all executive intelligence into one
central engineering brain.

This becomes the single entry point for
Repository Executive Intelligence.
"""


class RepositoryExecutiveBrain:

    def build(

        self,

        consciousness,

        experience,

        knowledge,

        strategy,

        priorities,

        planner,

        decision,

    ):

        brain = {

            "identity": {

                "phase":
                    consciousness["repository_identity"]["phase"],

                "technical_direction":
                    consciousness["repository_identity"]["technical_direction"],

                "brain_state":
                    consciousness["repository_identity"]["brain_state"],

            },

            "experience":

                experience,

            "knowledge":

                knowledge,

            "strategy":

                strategy,

            "priorities":

                priorities,

            "planner":

                planner,

            "decision":

                decision,

            "future_direction":

                decision["next_engineering_action"],

            "summary":

                self._summary(

                    consciousness,

                    strategy,

                    decision,

                )

        }

        return brain

    # ----------------------------------------------------

    def _summary(

        self,

        consciousness,

        strategy,

        decision,

    ):

        return (

            f"The Repository Executive Brain is in the "

            f"{consciousness['repository_identity']['phase']} phase. "

            f"It recommends '{decision['next_engineering_action']}' "

            f"using the strategy "

            f"'{strategy['engineering_strategy']}'."

        )