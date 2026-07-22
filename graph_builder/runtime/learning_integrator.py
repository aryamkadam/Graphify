"""
Graphify

Phase 14

Stage P14.5

Learning Integrator

Converts execution feedback into reusable
engineering experience.

Author:
Graphify Core
"""


class LearningIntegrator:

    VERSION = "P14.5"

    def __init__(self):

        self.experience_memory = []

    # --------------------------------------------------

    def integrate(self, feedback):

        experience = {

            "title": feedback["title"],

            "worker": feedback["worker"],

            "status": feedback["status"],

            "summary": feedback["summary"],

            "metrics": feedback["metrics"],

            "source_timestamp": feedback["timestamp"],

        }

        self.experience_memory.append(experience)

        return {

            "status": "success",

            "experience_created": True,

            "memory_size": len(self.experience_memory),

            "version": self.VERSION,

        }

    # --------------------------------------------------

    def experience(self):

        return self.experience_memory

    # --------------------------------------------------

    def status(self):

        return {

            "version": self.VERSION,

            "stored_experiences": len(self.experience_memory),

        }