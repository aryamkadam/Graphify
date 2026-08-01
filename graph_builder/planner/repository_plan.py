"""
Graphify

Phase 17

Stage P17.0

Repository Plan

Author:
Graphify Core
"""


class RepositoryPlan:

    VERSION = "P17.0"

    def __init__(

        self,

        repository,

        decision,

        objective,

        engineering_strategy,

        sprints,

        workers,

        dependencies,

        expected_result,

        priority,

        confidence,

    ):

        self.repository = repository
        self.decision = decision
        self.objective = objective
        self.engineering_strategy = engineering_strategy
        self.sprints = sprints
        self.workers = workers
        self.dependencies = dependencies
        self.expected_result = expected_result
        self.priority = priority
        self.confidence = confidence

    # ------------------------------------------

    def summary(self):

        return {

            "repository": self.repository,

            "objective": self.objective,

            "strategy": self.engineering_strategy,

            "sprints": len(self.sprints),

            "workers": len(self.workers),

            "priority": self.priority,

            "confidence": self.confidence,

            "version": self.VERSION,

        }