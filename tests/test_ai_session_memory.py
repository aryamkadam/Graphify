from pprint import pprint

from graph_builder.ai_session_memory import (
    generate_ai_session_memory
)

memory = (
    generate_ai_session_memory()
)

print(
    "\nAI Session Memory Generated\n"
)

pprint(
    memory
)