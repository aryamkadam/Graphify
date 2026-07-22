"""
Graphify

Phase 13

Stage P13.4

Engineering Decision Engine

Transforms engineering reasoning,
repository mission,
repository goals,
and engineering knowledge
into engineering decisions.

Author:
Graphify Core
"""

from graph_builder.knowledge.engineering_knowledge_retriever import (
    EngineeringKnowledgeRetriever,
)


class EngineeringDecisionEngine:

    VERSION = "P13.4"

    def __init__(
        self,
        reasoning=None,
        mission=None,
        goals=None,
    ):
        self.retriever = EngineeringKnowledgeRetriever()

        self.reasoning = reasoning
        self.mission = mission
        self.goals = goals

    # --------------------------------------------------

    def remember(self, review):
        return self.retriever.remember(review)

    # --------------------------------------------------

    def decide(self, task):

        previous = self.retriever.retrieve_by_title(
            task["title"]
        )

        decision_context = {
            "mission": self.mission,
            "goals": self.goals,
            "reasoning": self.reasoning,
        }

        if previous:

            recommendation = {
                "strategy":
                    "Reuse previous engineering experience",

                "experience_found":
                    len(previous),

                "confidence":
                    "HIGH",

                "reasoning_used":
                    self.reasoning is not None,

                "goal_alignment":
                    self.goals is not None,

                "mission_alignment":
                    self.mission is not None,
            }

        else:

            recommendation = {
                "strategy":
                    "Create new engineering solution",

                "experience_found":
                    0,

                "confidence":
                    "NORMAL",

                "reasoning_used":
                    self.reasoning is not None,

                "goal_alignment":
                    self.goals is not None,

                "mission_alignment":
                    self.mission is not None,
            }

        return {

            "status": "success",

            "task": task["title"],

            "decision_context": decision_context,

            "recommendation": recommendation,

            "version": self.VERSION,
        }

    # --------------------------------------------------

    def status(self):

        return {

            "version": self.VERSION,

            "knowledge":
                self.retriever.knowledge_summary(),

            "reasoning_available":
                self.reasoning is not None,

            "mission_available":
                self.mission is not None,

            "goals_available":
                self.goals is not None,
        }