"""
Graphify

Phase 5

Stage P5.7

Executive Index Engine

Indexes executive memory for efficient
future recall.

Author:
Graphify Core
"""


class ExecutiveIndexEngine:

    VERSION = "P5.7"

    # --------------------------------------------------

    def build(

        self,

        executive_memory,

    ):

        index = {

            "strategy": {},

            "priority": {},

        }

        memories = executive_memory.get(

            "executive_memory",

            [],

        )

        for i, memory in enumerate(memories):

            strategy = memory.get(

                "adaptation_strategy",

                "Unknown",

            )

            priority = memory.get(

                "priority",

                "NORMAL",

            )

            index["strategy"].setdefault(

                strategy,

                [],

            ).append(i)

            index["priority"].setdefault(

                priority,

                [],

            ).append(i)

        return {

            "index": index,

            "memory_count": len(memories),

            "version": self.VERSION,

        }