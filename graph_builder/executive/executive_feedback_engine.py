"""
Graphify

Phase 5

Stage P5.0

Executive Feedback Engine

Analyzes worker evolution after each
engineering sprint and produces
repository-level engineering insights.

Backward compatible with Phase 3.

Author:
Graphify Core
"""


class ExecutiveFeedbackEngine:

    VERSION = "P5.0"

    def __init__(self, registry):

        self.registry = registry

    # --------------------------------------------------

    def analyze(self):

        insights = []

        for worker_name in self.registry.all_workers():

            worker = self.registry.get(worker_name)

            profile = {}

            if hasattr(worker, "identity"):

                profile = worker.identity.profile()

            insights.append(

                {

                    "worker": worker_name,

                    "confidence": profile.get("confidence", 0),

                    "experience": profile.get("experience", 0),

                    "knowledge": profile.get("knowledge", 0),

                }

            )

        return {

            "workers": insights,

            "repository_recommendation":

                self._recommend(insights),

            "average_confidence":

                self._average_confidence(insights),

            "version":

                self.VERSION,

        }

    # --------------------------------------------------

    def build(self):
        """
        Phase 5 alias.

        AutonomousEngineeringLoop expects build().

        Phase 3 tests can still use analyze().
        """

        return self.analyze()

    # --------------------------------------------------

    def _average_confidence(

        self,

        workers,

    ):

        if not workers:

            return 0

        return sum(

            worker["confidence"]

            for worker in workers

        ) / len(workers)

    # --------------------------------------------------

    def _recommend(

        self,

        workers,

    ):

        if not workers:

            return "No engineering data available."

        average = self._average_confidence(

            workers

        )

        if average >= 80:

            return (

                "Repository ready for autonomous expansion."

            )

        elif average >= 60:

            return (

                "Repository engineering is progressing well."

            )

        elif average >= 50:

            return (

                "Continue engineering evolution."

            )

        return (

            "Improve worker capabilities."

        )