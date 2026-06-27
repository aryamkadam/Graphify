from pprint import pprint

from graph_builder.universal_context_schema import (
    generate_universal_context_schema
)

from graph_builder.protocols.uacp.translator import (
    translate_context
)

schema = generate_universal_context_schema()

result = translate_context(

    "chatgpt",

    "claude",

    schema

)

print()

print("Translation Engine")

print()

pprint(
    result["metadata"]
)
print()

print("Verification")

print()

print(
    result["metadata"]["verification"]
)