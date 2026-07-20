"""
Graphify

Phase 5.1

Worker Evolution Engine

Responsible for evolving workers after
completed engineering sprints.

Author:
Graphify Core
"""


class WorkerEvolutionEngine:

    VERSION = "P5.1"

    def __init__(

        self,

        registry,

    ):

        self.registry = registry

    # --------------------------------------------------

    def evolve(self, execution_report):

        evolved = []

        reports = execution_report.get(

            "report",

            [],

        )

        for result in reports:

            worker_name = result.get(

                "worker"

            )

            worker = self.registry.get(

                worker_name

            )

            if worker is None:

                continue

            if not hasattr(

                worker,

                "identity",

            ):

                continue

            identity = worker.identity

            profile = identity.profile()

            identity.update(

                experience=profile.get(

                    "experience",

                    0,

                ) + 1,

                knowledge=profile.get(

                    "knowledge",

                    0,

                ) + 2,

                confidence=min(

                    profile.get(

                        "confidence",

                        50,

                    ) + 5,

                    100,

                ),

            )

            evolved.append(

                {

                    "worker": worker_name,

                    "experience":

                        identity.profile()[

                            "experience"

                        ],

                    "knowledge":

                        identity.profile()[

                            "knowledge"

                        ],

                    "confidence":

                        identity.profile()[

                            "confidence"

                        ],

                }

            )

        return {

            "workers": evolved,

            "version": self.VERSION,

        }