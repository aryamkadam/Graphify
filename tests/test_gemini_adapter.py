from pprint import pprint

from graph_builder.universal_context_schema import (
    generate_universal_context_schema
)

from graph_builder.protocols.uacp.adapters.gemini import (
    gemini_to_uacp
)

schema = generate_universal_context_schema()

uacp = gemini_to_uacp(
    schema
)

print()

print("Gemini Adapter")

print()

pprint(
    uacp["metadata"]
)