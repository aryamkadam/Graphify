"""
Stage 19.4.1

Base AI Adapter

Every AI adapter inherits from this class.

Repository knowledge NEVER changes.

Only the presentation changes.
"""


class BaseAdapter:

    AI_NAME = "Generic"

    REASONING_STYLE = "Universal"

    def adapt(

        self,

        context,

    ):

        """
        Convert Universal Repository Context
        into an AI-specific export package.
        """

        return {

            "target_ai": self.AI_NAME,

            "reasoning_style": self.REASONING_STYLE,

            "repository_context": context,

        }

    # -----------------------------------------

    def adapter_metadata(self):

        return {

            "adapter": self.AI_NAME,

            "version": "19.4.1",

            "portable": True,

        }