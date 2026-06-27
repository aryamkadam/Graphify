from pprint import pprint

from graph_builder.context.builder import (
    build_context
)

context = build_context()

print("\nGraphify Context\n")

pprint(context)