"""
Graphify

Phase 10

Stage P10.1

Executive Decision

Canonical representation of an
engineering decision.

Author:
Graphify Core
"""

from datetime import datetime
import uuid


class ExecutiveDecision:

    VERSION = "P10.1"

    def __init__(

        self,

        decision_type,

        objective,

        priority,

        reasoning,

        actions,

    ):

        self.decision_id = str(uuid.uuid4())

        self.decision_type = decision_type

        self.objective = objective

        self.priority = priority

        self.reasoning = reasoning

        self.actions = actions

        self.created_at = datetime.utcnow().isoformat() + "Z"

    # --------------------------------------------------

    def summary(self):

        return {

            "decision_type": self.decision_type,

            "priority": self.priority,

            "objective": self.objective,

            "version": self.VERSION,

        }

    # --------------------------------------------------

    def to_dict(self):

        return {

            "decision_id": self.decision_id,

            "decision_type": self.decision_type,

            "objective": self.objective,

            "priority": self.priority,

            "reasoning": self.reasoning,

            "actions": self.actions,

            "created_at": self.created_at,

            "version": self.VERSION,

        }