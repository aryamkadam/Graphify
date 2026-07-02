"""
Stage 19.4.2

ChatGPT Adapter

Optimizes the Universal Repository Context
for ChatGPT.

Repository knowledge NEVER changes.

Only presentation changes.
"""

from graph_builder.context.adapters.base_adapter import (
    BaseAdapter,
)


class ChatGPTAdapter(BaseAdapter):

    AI_NAME = "ChatGPT"

    REASONING_STYLE = "Step-by-step Engineering"

    # -------------------------------------

    def adapt(

        self,

        context,

    ):

        return {

            "target_ai": self.AI_NAME,

            "reasoning_style": self.REASONING_STYLE,

            "system_prompt":

                self._system_prompt(),

            "repository_summary":

                context.get(

                    "repository_summary"

                ),

            "future_direction":

                context.get(

                    "future_direction"

                ),

            "repository_identity":

                context.get(

                    "repository_identity"

                ),

            "repository_strategy":

                context.get(

                    "repository_strategy"

                ),

            "repository_priorities":

                context.get(

                    "repository_priorities"

                ),

            "repository_decision":

                context.get(

                    "repository_decision"

                ),

            "repository_planner":

                context.get(

                    "repository_planner"

                ),

            "repository_memory":

                context.get(

                    "repository_memory"

                ),

            "repository_story":

                context.get(

                    "repository_story"

                ),

            "repository_consciousness":

                context.get(

                    "repository_consciousness"

                ),

            "full_repository_context":

                context,

        }

    # -------------------------------------

    def _system_prompt(self):

        return (

            "You are continuing work on an existing "

            "software repository. "

            "Preserve engineering decisions, "

            "repository memory, "

            "architecture, "

            "and long-term direction. "

            "Never restart analysis from scratch."

        )