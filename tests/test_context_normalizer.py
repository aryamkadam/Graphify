from pprint import pprint

from graph_builder.context_normalizer import (
    normalize_context
)

chatgpt_context = {

    "project":
        "Graphify",

    "stage":
        "stage-6.6-stable"
}

claude_context = {

    "project_name":
        "Graphify",

    "current_stage":
        "stage-6.6-stable"
}

gemini_context = {

    "workspace":
        "Graphify",

    "status":
        "stage-6.6-stable"
}

print(
    "\nChatGPT Normalized\n"
)

pprint(
    normalize_context(
        chatgpt_context,
        "ChatGPT"
    )
)

print(
    "\nClaude Normalized\n"
)

pprint(
    normalize_context(
        claude_context,
        "Claude"
    )
)

print(
    "\nGemini Normalized\n"
)

pprint(
    normalize_context(
        gemini_context,
        "Gemini"
    )
)