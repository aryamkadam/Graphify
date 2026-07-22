"""
Graphify

Phase 14

Stage P14.2

Worker Dispatcher

Assigns engineering tasks to the most
appropriate engineering worker.

Author:
Graphify Core
"""


class WorkerDispatcher:

    VERSION = "P14.2"

    def __init__(self):

        self.worker_rules = {

            "architecture": "Repository Architect",

            "refactor": "Code Engineer",

            "technical debt": "Code Engineer",

            "security": "Security Engineer",

            "test": "Testing Engineer",

            "performance": "Performance Engineer",

            "documentation": "Documentation Engineer",

            "deploy": "DevOps Engineer",

        }

    # --------------------------------------------------

    def dispatch(self, task):

        title = task.title.lower()

        description = task.description.lower()

        text = f"{title} {description}"

        for keyword, worker in self.worker_rules.items():

            if keyword in text:

                task.assigned_worker = worker

                return {

                    "status": "success",

                    "assigned_worker": worker,

                    "reason": f"Matched keyword '{keyword}'",

                    "version": self.VERSION,

                }

        task.assigned_worker = "General Engineer"

        return {

            "status": "success",

            "assigned_worker": "General Engineer",

            "reason": "No specialized worker matched",

            "version": self.VERSION,

        }

    # --------------------------------------------------

    def dispatcher_status(self):

        return {

            "version": self.VERSION,

            "workers": list(set(self.worker_rules.values())),

            "supported_keywords": list(self.worker_rules.keys()),

        }