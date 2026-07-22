"""
Graphify

Phase 14

Stage P14.3

Execution Monitor

Monitors engineering task execution.

This component observes execution.

It never performs execution.

Author:
Graphify Core
"""


from datetime import datetime


class ExecutionMonitor:

    VERSION = "P14.3"

    def __init__(self):

        self.execution_history = []

    # --------------------------------------------------

    def start(self, task):

        event = {

            "task_id": task.task_id,

            "title": task.title,

            "worker": task.assigned_worker,

            "status": "RUNNING",

            "started_at": datetime.utcnow().isoformat() + "Z",

        }

        self.execution_history.append(event)

        return event

    # --------------------------------------------------

    def complete(self, task):

        event = {

            "task_id": task.task_id,

            "title": task.title,

            "worker": task.assigned_worker,

            "status": "COMPLETED",

            "completed_at": datetime.utcnow().isoformat() + "Z",

        }

        self.execution_history.append(event)

        return event

    # --------------------------------------------------

    def fail(self, task, reason):

        event = {

            "task_id": task.task_id,

            "title": task.title,

            "worker": task.assigned_worker,

            "status": "FAILED",

            "reason": reason,

            "failed_at": datetime.utcnow().isoformat() + "Z",

        }

        self.execution_history.append(event)

        return event

    # --------------------------------------------------

    def history(self):

        return self.execution_history

    # --------------------------------------------------

    def monitor_status(self):

        return {

            "version": self.VERSION,

            "events_recorded": len(self.execution_history),

        }