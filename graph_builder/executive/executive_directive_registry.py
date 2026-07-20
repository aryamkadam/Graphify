"""
Graphify

Phase 5

Stage P5.14

Executive Directive Registry

Stores and tracks executive directives.

Author:
Graphify Core
"""


class ExecutiveDirectiveRegistry:

    VERSION = "P5.14"

    def __init__(self):

        self._directives = []

        self._counter = 1

    # --------------------------------------------------

    def register(

        self,

        directive_report,

    ):

        directive = {

            "directive_id":

                f"DIR-{self._counter:04d}",

            "strategy":

                directive_report.get(

                    "strategy"

                ),

            "priority":

                directive_report.get(

                    "priority"

                ),

            "confidence":

                directive_report.get(

                    "confidence"

                ),

            "directive":

                directive_report.get(

                    "directive"

                ),

            "status":

                "READY",

        }

        self._counter += 1

        self._directives.append(

            directive

        )

        return directive

    # --------------------------------------------------

    def directives(self):

        return list(

            self._directives

        )

    # --------------------------------------------------

    def latest(self):

        if not self._directives:

            return None

        return self._directives[-1]

    # --------------------------------------------------

    def summary(self):

        ready = sum(

            1

            for d in self._directives

            if d["status"] == "READY"

        )

        return {

            "total_directives":

                len(self._directives),

            "ready":

                ready,

            "version":

                self.VERSION,

        }