"""
Graphify

Phase 14

Stage P14.4

Feedback Collector

Collects structured feedback from completed
engineering executions.

This component never learns.

It only captures execution outcomes.

Author:
Graphify Core
"""

from datetime import datetime


class FeedbackCollector:

    VERSION = "P14.4"

    def __init__(self):

        self.feedback_history = []

    # --------------------------------------------------

    def collect(

        self,

        task,

        success=True,

        summary="",

        metrics=None,

    ):

        if metrics is None:
            metrics = {}

        feedback = {

            "task_id": task.task_id,

            "title": task.title,

            "worker": task.assigned_worker,

            "status": "SUCCESS" if success else "FAILED",

            "summary": summary,

            "metrics": metrics,

            "timestamp": datetime.utcnow().isoformat() + "Z",

        }

        self.feedback_history.append(feedback)

        return feedback

    # --------------------------------------------------

    def history(self):

        return self.feedback_history

    # --------------------------------------------------

    def collector_status(self):

        successful = sum(
            1
            for item in self.feedback_history
            if item["status"] == "SUCCESS"
        )

        failed = len(self.feedback_history) - successful

        return {

            "version": self.VERSION,

            "feedback_entries": len(self.feedback_history),

            "successful": successful,

            "failed": failed,

        }