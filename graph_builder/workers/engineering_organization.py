"""
Graphify

Phase 7

Stage P7.9

Engineering Organization

Represents the complete engineering
organization inside Graphify.

Author:
Graphify Core
"""


class EngineeringOrganization:

    VERSION = "P7.9"

    def __init__(

        self,

        workers,

    ):

        self.workers = workers

    # --------------------------------------------------

    def summary(self):

        return {

            "organization_size": len(self.workers),

            "workers": [

                {

                    "worker": worker.worker_name,

                    "role": worker.role,

                    "status": worker.status,

                }

                for worker in self.workers

            ],

            "version": self.VERSION,

        }

    # --------------------------------------------------

    def available_workers(self):

        return [

            worker

            for worker in self.workers

            if worker.status == "IDLE"

        ]

    # --------------------------------------------------

    def worker_roles(self):

        return {

            worker.worker_name: worker.role

            for worker in self.workers

        }