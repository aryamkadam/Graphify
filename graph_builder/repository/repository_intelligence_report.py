"""
Graphify

Phase 9

Stage P9.7

Repository Intelligence Report

Canonical engineering understanding
of the repository.

Author:
Graphify Core
"""


class RepositoryIntelligenceReport:

    VERSION = "P9.7"

    def __init__(

        self,

        repository_name,

        engineering_stage,

        engineering_health,

        engineering_strategy,

        executive_summary,

        historical_context,

        recommendations,

    ):

        self.repository_name = repository_name
        self.engineering_stage = engineering_stage
        self.engineering_health = engineering_health
        self.engineering_strategy = engineering_strategy
        self.executive_summary = executive_summary
        self.historical_context = historical_context
        self.recommendations = recommendations

    # ----------------------------------------------

    def summary(self):

        return {

            "repository": self.repository_name,

            "stage": self.engineering_stage,

            "health": self.engineering_health,

            "strategy": self.engineering_strategy,

            "version": self.VERSION,

        }

    # ----------------------------------------------

    def to_dict(self):

        return {

            "repository": self.repository_name,

            "engineering_stage": self.engineering_stage,

            "engineering_health": self.engineering_health,

            "engineering_strategy": self.engineering_strategy,

            "executive_summary": self.executive_summary,

            "historical_context": self.historical_context,

            "recommendations": self.recommendations,

            "version": self.VERSION,

        }