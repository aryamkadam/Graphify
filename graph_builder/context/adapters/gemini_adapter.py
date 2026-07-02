"""
Stage 19.4.4

Gemini Adapter

Optimizes the Universal Repository Context
for Gemini.

Repository knowledge NEVER changes.

Only presentation changes.
"""

from graph_builder.context.adapters.base_adapter import (
    BaseAdapter,
)


class GeminiAdapter(BaseAdapter):

    AI_NAME = "Gemini"

    REASONING_STYLE = "Structured Engineering"

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

            # Gemini prefers structured engineering objects

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

            "repository_planner":

                context.get(

                    "repository_planner"

                ),

            "repository_decision":

                context.get(

                    "repository_decision"

                ),

            "repository_memory":

                context.get(

                    "repository_memory"

                ),

            "repository_consciousness":

                context.get(

                    "repository_consciousness"

                ),

            "repository_story":

                context.get(

                    "repository_story"

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

            "Prioritize structured engineering reasoning, repository "

            "relationships, planning, architecture, and long-term "

            "repository evolution. Never restart repository analysis "

            "from scratch."

        )