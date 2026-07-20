"""
Graphify

Phase 4.3

Engineering Risk Analyzer

Evaluates an engineering sprint before
execution.

Author:
Graphify Core
"""


class EngineeringRiskAnalyzer:

    VERSION = "P4.3"

    def __init__(self, sprint):

        self.sprint = sprint

    # --------------------------------------------------

    def _risk_level(self):

        task_count = len(

            self.sprint.get(

                "tasks",

                []

            )

        )

        if task_count >= 8:

            return "HIGH"

        elif task_count >= 5:

            return "MEDIUM"

        return "LOW"

    # --------------------------------------------------

    def _complexity(self):

        task_count = len(

            self.sprint.get(

                "tasks",

                []

            )

        )

        if task_count >= 10:

            return "HIGH"

        elif task_count >= 5:

            return "MEDIUM"

        return "LOW"

    # --------------------------------------------------

    def _estimated_duration(self):

        complexity = self._complexity()

        if complexity == "HIGH":

            return "LONG"

        elif complexity == "MEDIUM":

            return "MEDIUM"

        return "SHORT"

    # --------------------------------------------------

    def _recommendation(self):

        risk = self._risk_level()

        if risk == "HIGH":

            return "Split sprint before execution."

        elif risk == "MEDIUM":

            return "Execute with monitoring."

        return "Sprint approved."

    # --------------------------------------------------

    def build(self):

        return {

            "risk_level":

                self._risk_level(),

            "complexity":

                self._complexity(),

            "estimated_duration":

                self._estimated_duration(),

            "recommendation":

                self._recommendation(),

            "version":

                self.VERSION,

        }