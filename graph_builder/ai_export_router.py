from graph_builder.ai_export_chatgpt import (
    export_chatgpt_context
)

from graph_builder.ai_export_claude import (
    export_claude_context
)

from graph_builder.ai_export_gemini import (
    export_gemini_context
)


def export_for_ai(
    context,
    target_ai
):

    if target_ai == "ChatGPT":
        return export_chatgpt_context(
            context
        )

    if target_ai == "Claude":
        return export_claude_context(
            context
        )

    if target_ai == "Gemini":
        return export_gemini_context(
            context
        )

    return "Unsupported AI"