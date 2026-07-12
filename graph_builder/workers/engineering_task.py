"""
Graphify

Stage 25.1

Engineering Task

Represents one engineering unit of work.

Author:
Graphify Core
"""

import uuid

from datetime import datetime


class EngineeringTask:

    VERSION = "25.1"

    def __init__(

        self,

        title,

        description="",

        priority="MEDIUM",

    ):

        self.task_id = str(uuid.uuid4())

        self.title = title

        self.description = description

        self.priority = priority

        self.status = "PENDING"

        self.assigned_worker = None

        self.created_at = datetime.utcnow().isoformat() + "Z"

    # --------------------------------------------------

    def assign(

        self,

        worker_name,

    ):

        self.assigned_worker = worker_name

        self.status = "ASSIGNED"

    # --------------------------------------------------

    def start(self):

        self.status = "IN_PROGRESS"

    # --------------------------------------------------

    def complete(self):

        self.status = "COMPLETED"

    # --------------------------------------------------

    def to_dict(self):

        return {

            "task_id": self.task_id,

            "title": self.title,

            "description": self.description,

            "priority": self.priority,

            "status": self.status,

            "assigned_worker": self.assigned_worker,

            "created_at": self.created_at,

            "version": self.VERSION,

        }