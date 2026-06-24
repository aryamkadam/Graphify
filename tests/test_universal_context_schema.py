from pprint import pprint

from graph_builder.universal_context_schema import (
    generate_universal_context_schema
)

print(
    "\nUniversal Context Schema Generated\n"
)

pprint(
    generate_universal_context_schema()
)