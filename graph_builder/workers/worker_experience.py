"""
Graphify

Phase 2

Stage P2.5

Worker Experience Engine

Transforms accumulated work into
engineering maturity.

Author:
Graphify Core
"""


class WorkerExperience:

    VERSION = "P2.5"

    def __init__(self):

        self.experience_points = 0

        self.level = 1

        self.confidence = 50

    # --------------------------------------------------

    def gain(

        self,

        points=10,

    ):

        self.experience_points += points

        self.level = (

            self.experience_points // 100

        ) + 1

        self.confidence = min(

            100,

            50 + self.level * 2,

        )

    # --------------------------------------------------

    def maturity(self):

        if self.level < 3:
            return "JUNIOR"

        if self.level < 6:
            return "MID"

        if self.level < 10:
            return "SENIOR"

        return "PRINCIPAL"

    # --------------------------------------------------

    def profile(self):

        return {

            "experience_points": self.experience_points,

            "level": self.level,

            "confidence": self.confidence,

            "maturity": self.maturity(),

            "version": self.VERSION,

        }