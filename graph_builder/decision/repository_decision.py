"""
Graphify

Phase 16

Stage P16.0

Repository Decision

Author:
Graphify Core
"""


class RepositoryDecision:

    VERSION = "P16.0"

    def __init__(

        self,

        repository,

        selected_goal,

        decision,

        decision_reason,

        priority,

        confidence,

    ):

        self.repository = repository

        self.selected_goal = selected_goal

        self.decision = decision

        self.decision_reason = decision_reason

        self.priority = priority

        self.confidence = confidence

    # -----------------------------------------

    def summary(self):

        return {

            "repository": self.repository,

            "selected_goal": self.selected_goal,

            "decision": self.decision,

            "priority": self.priority,

            "confidence": self.confidence,

            "version": self.VERSION,

        }