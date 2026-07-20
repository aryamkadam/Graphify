"""
Graphify

Phase 11

Stage P11.7

Repository Architecture Report

Author:
Graphify Core
"""


class RepositoryArchitectureReport:

    VERSION = "P11.7"

    def __init__(

        self,

        repository,

        health_score,

        duplicate_responsibilities,

        oversized_layers,

        architecture_cycles,

        recommendations,

    ):

        self.repository = repository

        self.health_score = health_score

        self.duplicate_responsibilities = duplicate_responsibilities

        self.oversized_layers = oversized_layers

        self.architecture_cycles = architecture_cycles

        self.recommendations = recommendations

    def export(self):

        return {

            "repository": self.repository,

            "architecture_health": self.health_score,

            "duplicate_responsibilities":

                self.duplicate_responsibilities,

            "oversized_layers":

                self.oversized_layers,

            "architecture_cycles":

                self.architecture_cycles,

            "recommendations":

                self.recommendations,

            "version":

                self.VERSION,

        }