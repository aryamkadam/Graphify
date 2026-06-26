from pprint import pprint

from graph_builder.universal_context_schema import (
    generate_universal_context_schema
)

from graph_builder.protocols.uacp.adapters.claude import (
    claude_to_uacp
)

schema = generate_universal_context_schema()

uacp = claude_to_uacp(
    schema
)

print()

print("Claude Adapter")

print()

pprint(
    uacp["metadata"]
)