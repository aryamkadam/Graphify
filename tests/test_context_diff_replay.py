from pprint import pprint

from graph_builder.context_diff_replay import (
    generate_context_diff_replay
)

result = (
    generate_context_diff_replay()
)

print(
    "\nContext Diff Replay Generated\n"
)

pprint(
    result
)