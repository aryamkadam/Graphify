"""
Graphify

Phase 7

Stage P7.4

Engineering Task Evolution

Standard engineering work package
used throughout Graphify.

Every engineering worker communicates
using EngineeringTask.

Backward compatible with Stage 25.1.

Author:
Graphify Core
"""

import uuid
from datetime import datetime


class EngineeringTask:

    VERSION = "P7.4"

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

        # ------------------------------------------
        # Phase 7 Extensions
        # ------------------------------------------

        self.complexity = "MEDIUM"

        self.dependencies = []

        self.expected_output = None

        self.actual_output = None

        self.parent_task = None

        self.tags = []

        self.estimated_effort = None

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

    def complete(

        self,

        output=None,

    ):

        self.status = "COMPLETED"

        self.actual_output = output

    # --------------------------------------------------

    def add_dependency(

        self,

        task_id,

    ):

        if task_id not in self.dependencies:

            self.dependencies.append(task_id)

    # --------------------------------------------------

    def add_tag(

        self,

        tag,

    ):

        if tag not in self.tags:

            self.tags.append(tag)

    # --------------------------------------------------

    def set_complexity(

        self,

        complexity,

    ):

        self.complexity = complexity

    # --------------------------------------------------

    def set_expected_output(

        self,

        expected,

    ):

        self.expected_output = expected

    # --------------------------------------------------

    def set_estimated_effort(

        self,

        effort,

    ):

        self.estimated_effort = effort

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

            "complexity": self.complexity,

            "dependencies": self.dependencies,

            "expected_output": self.expected_output,

            "actual_output": self.actual_output,

            "parent_task": self.parent_task,

            "tags": self.tags,

            "estimated_effort": self.estimated_effort,

            "version": self.VERSION,

        }