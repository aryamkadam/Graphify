"""
Graphify

Stage 28.2

Engineering Knowledge Retriever

Provides a clean interface between
AI workers and Engineering Memory.

Author:
Graphify Core
"""

from graph_builder.memory.engineering_memory import EngineeringMemory


class EngineeringKnowledgeRetriever:

    VERSION = "28.2"

    def __init__(self):

        self.memory = EngineeringMemory()

    # --------------------------------------------------

    def remember(

        self,

        review,

    ):

        return self.memory.remember(review)

    # --------------------------------------------------

    def retrieve_by_title(

        self,

        title,

    ):

        return self.memory.find_by_title(title)

    # --------------------------------------------------

    def retrieve_by_status(

        self,

        status,

    ):

        return self.memory.find_by_status(status)

    # --------------------------------------------------

    def retrieve_by_worker(

        self,

        worker,

    ):

        return self.memory.find_by_worker(worker)

    # --------------------------------------------------

    def latest_experience(self):

        return self.memory.latest()

    # --------------------------------------------------

    def knowledge_summary(self):

        return {

            "status": "success",

            "memory": self.memory.status(),

            "version": self.VERSION,

        }