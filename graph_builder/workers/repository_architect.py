"""
Graphify

Phase 7

Stage P7.2

Repository Architect

Graphify's architecture specialist.

Responsible for understanding and
evaluating repository structure.

Author:
Graphify Core
"""

from graph_builder.workers.engineering_worker import EngineeringWorker


class RepositoryArchitect(EngineeringWorker):

    VERSION = "P7.2"

    def __init__(self):

        super().__init__(

            worker_name="Repository Architect",

            role="Architecture",

        )

    # --------------------------------------------------

    def assess_repository(

        self,

        repository_phase,

        technical_direction,

    ):

        assessment = {

            "repository_phase": repository_phase,

            "technical_direction": technical_direction,

            "architectural_health": self._health(

                repository_phase,

                technical_direction,

            ),

            "recommendation": self._recommendation(

                repository_phase,

            ),

            "worker": self.worker_name,

            "version": self.VERSION,

        }

        return assessment

    # --------------------------------------------------

    def _health(

        self,

        repository_phase,

        technical_direction,

    ):

        if (

            repository_phase == "Growth"

            and technical_direction == "Positive"

        ):

            return "EXCELLENT"

        elif technical_direction == "Positive":

            return "GOOD"

        elif technical_direction == "Neutral":

            return "STABLE"

        return "NEEDS IMPROVEMENT"

    # --------------------------------------------------

    def _recommendation(

        self,

        repository_phase,

    ):

        mapping = {

            "Initialization":

                "Focus on repository foundation.",

            "Stabilization":

                "Strengthen repository architecture.",

            "Growth":

                "Expand engineering capabilities.",

            "Optimization":

                "Optimize large-scale architecture.",

        }

        return mapping.get(

            repository_phase,

            "Continue repository evolution.",

        )