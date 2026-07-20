"""
Graphify

Phase 7

Stage P7.8

Worker Experience Sharing Engine

Allows engineering workers to
share completed experience.

Author:
Graphify Core
"""


class WorkerExperienceSharingEngine:

    VERSION = "P7.8"

    def share(

        self,

        source_memory,

        target_memory,

    ):

        shared = 0

        existing = {

            task["title"]

            for task in target_memory.history()

        }

        for task in source_memory.history():

            if task["title"] not in existing:

                target_memory._history.append(

                    task.copy()

                )

                shared += 1

        return {

            "shared_tasks": shared,

            "source_worker": source_memory.worker_name,

            "target_worker": target_memory.worker_name,

            "version": self.VERSION,

        }