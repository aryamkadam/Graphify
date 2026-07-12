"""
Graphify

Phase 3

Stage P3.8

Executive Feedback Engine

Analyzes worker evolution after each
engineering sprint and produces
repository-level insights.

Author:
Graphify Core
"""


class ExecutiveFeedbackEngine:

    VERSION = "P3.8"

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

            insights.append({

                "worker": worker_name,

                "confidence": profile.get("confidence", 0),

                "experience": profile.get("experience", 0),

                "knowledge": profile.get("knowledge", 0),

            })

        return {

            "workers": insights,

            "repository_recommendation":

                self._recommend(insights),

            "version": self.VERSION,

        }

    # --------------------------------------------------

    def _recommend(self, workers):

        if not workers:

            return "No engineering data available."

        average = sum(

            w["confidence"]

            for w in workers

        ) / len(workers)

        if average >= 70:

            return "Repository ready for expansion."

        elif average >= 50:

            return "Continue engineering evolution."

        else:

            return "Improve worker capabilities."