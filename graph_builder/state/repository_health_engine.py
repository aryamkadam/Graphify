"""
Graphify

Phase 20

Stage P20.2

Repository Health Engine

Calculates the current runtime health
of a repository.

Author:
Graphify Core
"""


class RepositoryHealthEngine:

    VERSION = "P20.2"

    # --------------------------------------------------

    def build(

        self,

        repository_context,

    ):

        score = 0.0

        #
        # Repository Intelligence
        #

        if getattr(

            repository_context,

            "repository_intelligence",

            None,

        ) is not None:

            score += 25

        #
        # Repository Brain
        #

        if getattr(

            repository_context,

            "repository_brain",

            None,

        ) is not None:

            score += 25

        #
        # Repository Cognitive Memory
        #

        if getattr(

            repository_context,

            "repository_memory",

            None,

        ) is not None:

            score += 20

        #
        # Repository Loaded
        #

        if getattr(

            repository_context,

            "repository_loaded",

            False,

        ):

            score += 20

        #
        # Repository Ready
        #

        if getattr(

            repository_context,

            "ready",

            False,

        ):

            score += 10

        return round(score, 2)

    # --------------------------------------------------

    def status(self):

        return {

            "engine": "Repository Health Engine",

            "version": self.VERSION,

        }