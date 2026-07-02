"""
Stage 19.4.5

Repository Adapter Factory

Creates the correct AI adapter
from a target AI name.

This isolates adapter creation
from the rest of Graphify.
"""

from graph_builder.context.adapters.chatgpt_adapter import (
    ChatGPTAdapter,
)

from graph_builder.context.adapters.claude_adapter import (
    ClaudeAdapter,
)

from graph_builder.context.adapters.gemini_adapter import (
    GeminiAdapter,
)


class RepositoryAdapterFactory:

    def __init__(self):

        self._adapters = {

            "chatgpt": ChatGPTAdapter,

            "claude": ClaudeAdapter,

            "gemini": GeminiAdapter,

        }

    # --------------------------------------------------

    def get(

        self,

        target_ai,

    ):

        key = target_ai.lower()

        if key not in self._adapters:

            raise ValueError(

                f"Unsupported AI adapter: {target_ai}"

            )

        return self._adapters[key]()

    # --------------------------------------------------

    def supported_adapters(self):

        return sorted(

            self._adapters.keys()

        )