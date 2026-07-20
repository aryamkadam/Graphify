"""
Graphify

Phase 5

Stage P5.8

Executive Recall Engine

Retrieves executive memories using
the Executive Index.

Author:
Graphify Core
"""


class ExecutiveRecallEngine:

    VERSION = "P5.8"

    # --------------------------------------------------

    def recall_by_strategy(

        self,

        executive_memory,

        executive_index,

        strategy,

    ):

        memory = executive_memory.get(

            "executive_memory",

            [],

        )

        strategy_index = executive_index.get(

            "index",

            {},

        ).get(

            "strategy",

            {},

        )

        positions = strategy_index.get(

            strategy,

            [],

        )

        results = [

            memory[position]

            for position in positions

            if position < len(memory)

        ]

        return {

            "query": strategy,

            "matches": len(results),

            "results": results,

            "version": self.VERSION,

        }

    # --------------------------------------------------

    def latest(

        self,

        executive_memory,

    ):

        memory = executive_memory.get(

            "executive_memory",

            [],

        )

        if not memory:

            return None

        return memory[-1]