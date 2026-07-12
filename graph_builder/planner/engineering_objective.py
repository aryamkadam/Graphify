"""
Graphify

Stage 36.0

Engineering Objective

Represents a high-level engineering goal.

Author:
Graphify Core
"""

import uuid
from datetime import datetime


class EngineeringObjective:

    VERSION = "36.0"

    def __init__(

        self,

        title,

        description,

        priority="HIGH",

    ):

        self.objective_id = str(uuid.uuid4())

        self.title = title

        self.description = description

        self.priority = priority

        self.status = "ACTIVE"

        self.sprints = []

        self.created_at = (

            datetime.utcnow().isoformat() + "Z"

        )

    # --------------------------------------------------

    def add_sprint(

        self,

        sprint,

    ):

        self.sprints.append(sprint)

    # --------------------------------------------------

    def sprint_count(self):

        return len(self.sprints)

    # --------------------------------------------------

    def complete(self):

        self.status = "COMPLETED"

    # --------------------------------------------------

    def to_dict(self):

        return {

            "objective_id": self.objective_id,

            "title": self.title,

            "description": self.description,

            "priority": self.priority,

            "status": self.status,

            "sprints": self.sprint_count(),

            "created_at": self.created_at,

            "version": self.VERSION,

        }