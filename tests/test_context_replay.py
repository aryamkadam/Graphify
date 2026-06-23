from pprint import pprint

from graph_builder.context_replay import (
    generate_context_replay
)

result = (
    generate_context_replay()
)

print(
    "\nContext Replay Generated\n"
)

pprint(
    result
)