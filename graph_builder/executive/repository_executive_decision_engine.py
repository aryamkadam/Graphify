"""
Stage 18.4

Repository Executive Decision Engine

Acts as the CTO of the Repository Brain.

Uses strategy, priorities, planning and
repository consciousness to decide what
should happen next.
"""


class RepositoryExecutiveDecisionEngine:

    def build(

        self,

        planner,

        consciousness,

        knowledge,

        experience,

    ):

        decision = self._choose_primary_decision(planner)

        confidence = self._confidence(

            knowledge,

            experience,

        )

        return {

            "executive_decision": decision,

            "confidence": confidence,

            "repository_phase":
                consciousness["repository_identity"]["phase"],

            "next_engineering_action":
                decision["action"],

            "reason":
                decision["reason"],

            "summary":
                (
                    f"Repository recommends "
                    f"'{decision['action']}' "
                    f"with confidence {confidence:.2f}."
                )

        }

    # --------------------------------------------

    def _choose_primary_decision(

        self,

        planner,

    ):

        first_sprint = planner["sprints"][0]

        first_task = first_sprint["tasks"][0]

        return {

            "action": first_task["task"],

            "reason": first_task["reason"],

            "priority": first_task["priority"]

        }

    # --------------------------------------------

    def _confidence(

        self,

        knowledge,

        experience,

    ):

        knowledge_score = knowledge.get(

            "knowledge_confidence",

            0.8,

        )

        level = experience.get(

            "experience_level",

            "Junior",

        )

        multiplier = {

            "Junior": 0.8,

            "Intermediate": 0.9,

            "Senior": 1.0,

            "Expert": 1.1,

        }

        return round(

            knowledge_score *

            multiplier.get(level, 0.8),

            2,

        )