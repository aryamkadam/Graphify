from pprint import pprint

from graph_builder.context_timeline import (
    generate_context_timeline
)

result = (
    generate_context_timeline()
)

print(
    "\nContext Timeline Generated\n"
)

pprint(
    result
)