"""
Stage 19.4.3

Claude Adapter

Optimizes the Universal Repository Context
for Claude.

Repository knowledge NEVER changes.

Only presentation changes.
"""

from graph_builder.context.adapters.base_adapter import (
    BaseAdapter,
)


class ClaudeAdapter(BaseAdapter):

    AI_NAME = "Claude"

    REASONING_STYLE = "Long-form Architectural Reasoning"

    # -------------------------------------------------

    def adapt(

        self,

        context,

    ):

        return {

            "target_ai": self.AI_NAME,

            "reasoning_style": self.REASONING_STYLE,

            "system_prompt":

                self._system_prompt(),

            # Claude prefers understanding first

            "repository_story":

                context.get(

                    "repository_story"

                ),

            "repository_identity":

                context.get(

                    "repository_identity"

                ),

            "repository_consciousness":

                context.get(

                    "repository_consciousness"

                ),

            "repository_strategy":

                context.get(

                    "repository_strategy"

                ),

            "repository_decision":

                context.get(

                    "repository_decision"

                ),

            "repository_memory":

                context.get(

                    "repository_memory"

                ),

            "repository_planner":

                context.get(

                    "repository_planner"

                ),

            "repository_priorities":

                context.get(

                    "repository_priorities"

                ),

            "repository_summary":

                context.get(

                    "repository_summary"

                ),

            "future_direction":

                context.get(

                    "future_direction"

                ),

            "full_repository_context":

                context,

        }

    # -------------------------------------------------

    def _system_prompt(self):

        return (

            "You are continuing work on an existing software repository. "

            "Understand its evolution, engineering history, architectural "

            "direction, long-term goals, and repository memory before "

            "making engineering decisions. Never restart repository "

            "analysis from scratch."

        )