"""
Graphify

Stage 35.0

Engineering Sprint

Represents a collection of engineering
tasks executed toward a common goal.

Author:
Graphify Core
"""

import uuid
from datetime import datetime


class EngineeringSprint:

    VERSION = "35.0"

    def __init__(

        self,

        title,

        goal,

        duration_days=7,

    ):

        self.sprint_id = str(uuid.uuid4())

        self.title = title

        self.goal = goal

        self.duration_days = duration_days

        self.tasks = []

        self.created_at = (

            datetime.utcnow()

            .isoformat()

            + "Z"

        )

    # --------------------------------------------------

    def add_task(

        self,

        task,

    ):

        self.tasks.append(task)

    # --------------------------------------------------

    def task_count(self):

        return len(self.tasks)

    # --------------------------------------------------

    def to_dict(self):

        return {

            "sprint_id": self.sprint_id,

            "title": self.title,

            "goal": self.goal,

            "duration_days": self.duration_days,

            "tasks": self.task_count(),

            "created_at": self.created_at,

            "version": self.VERSION,

        }