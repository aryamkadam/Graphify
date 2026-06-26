from pprint import pprint

from graph_builder.universal_context_schema import (
    generate_universal_context_schema
)

from graph_builder.protocols.uacp.adapters.chatgpt import (
    chatgpt_to_uacp
)

schema = generate_universal_context_schema()

uacp = chatgpt_to_uacp(
    schema
)

print()

print("ChatGPT Adapter")

print()

pprint(
    uacp["metadata"]
)
