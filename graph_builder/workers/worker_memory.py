"""
Graphify

Phase 2

Stage P2.2

Worker Memory

Persistent engineering memory
for every worker.

Author:
Graphify Core
"""


class WorkerMemory:

    VERSION = "P2.2"

    def __init__(self):

        self._memories = []

    # ------------------------------------------

    def remember(

        self,

        category,

        content,

    ):

        self._memories.append(

            {

                "category": category,

                "content": content,

            }

        )

    # ------------------------------------------

    def recall(self):

        return list(self._memories)

    # ------------------------------------------

    def recall_category(

        self,

        category,

    ):

        return [

            memory

            for memory in self._memories

            if memory["category"] == category

        ]

    # ------------------------------------------

    def clear(self):

        self._memories.clear()

    # ------------------------------------------

    def status(self):

        return {

            "memories": len(self._memories),

            "version": self.VERSION,

        }