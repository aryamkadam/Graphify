"""
Graphify

Stage 29.0

Engineering Decision Engine

Creates engineering decisions using
previous engineering knowledge.

Author:
Graphify Core
"""

from graph_builder.knowledge.engineering_knowledge_retriever import (
    EngineeringKnowledgeRetriever,
)


class EngineeringDecisionEngine:

    VERSION = "29.0"

    def __init__(self):

        self.retriever = EngineeringKnowledgeRetriever()

    # --------------------------------------------------

    def remember(

        self,

        review,

    ):

        return self.retriever.remember(review)

    # --------------------------------------------------

    def decide(

        self,

        task,

    ):

        previous = self.retriever.retrieve_by_title(

            task["title"]

        )

        if previous:

            recommendation = {

                "strategy": "Reuse previous engineering experience",

                "experience_found": len(previous),

                "confidence": "HIGH",

            }

        else:

            recommendation = {

                "strategy": "Create new engineering solution",

                "experience_found": 0,

                "confidence": "NORMAL",

            }

        return {

            "status": "success",

            "task": task["title"],

            "recommendation": recommendation,

            "version": self.VERSION,

        }

    # --------------------------------------------------

    def status(self):

        return {

            "version": self.VERSION,

            "knowledge": self.retriever.knowledge_summary(),

        }