"""
Stage 19.1

Universal Repository Context

The complete Repository Brain packed into
one transferable object.

Every AI platform receives exactly this
context.
"""


class UniversalRepositoryContext:

    VERSION = "19.1"

    def build(

        self,

        executive_brain,

        repository_memory,

        repository_story,

        repository_consciousness,

    ):

        return {

            "context_version": self.VERSION,

            "repository_identity":

                executive_brain["identity"],

            "repository_strategy":

                executive_brain["strategy"],

            "repository_priorities":

                executive_brain["priorities"],

            "repository_planner":

                executive_brain["planner"],

            "repository_decision":

                executive_brain["decision"],

            "repository_memory":

                repository_memory,

            "repository_story":

                repository_story,

            "repository_consciousness":

                repository_consciousness,

            "future_direction":

                executive_brain["future_direction"],

            "repository_summary":

                executive_brain["summary"],

            "export_ready": True,

            "portable": True,

            "platform": "Universal"

        }