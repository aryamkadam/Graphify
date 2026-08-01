"""
Graphify

Phase 19

Stage P19.4

Repository Evolution Memory

Compares Repository Cognitive Memory snapshots
to understand repository evolution over time.

Responsibilities

• Compare consecutive snapshots
• Detect identity changes
• Detect capability changes
• Detect behavior changes
• Report repository evolution

Author:
Graphify Core
"""


class RepositoryEvolutionMemory:

    VERSION = "P19.4"

    # -----------------------------------------------------

    def compare(

        self,

        previous_snapshot,

        current_snapshot,

    ):

        if previous_snapshot is None:

            return {

                "repository":

                    current_snapshot.get("repository"),

                "first_snapshot": True,

                "identity_changed": False,

                "capability_changed": False,

                "behavior_changed": False,

                "timeline_length": 1,

                "version": self.VERSION,

            }

        return {

            "repository":

                current_snapshot.get("repository"),

            "first_snapshot": False,

            "previous_identity":

                previous_snapshot.get("identity"),

            "current_identity":

                current_snapshot.get("identity"),

            "identity_changed":

                previous_snapshot.get("identity")
                != current_snapshot.get("identity"),

            "capability_changed":

                previous_snapshot.get("capability")
                != current_snapshot.get("capability"),

            "behavior_changed":

                previous_snapshot.get("behavior")
                != current_snapshot.get("behavior"),

            "timeline_length": 2,

            "version": self.VERSION,

        }