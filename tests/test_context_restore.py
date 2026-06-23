from pprint import pprint

from graph_builder.context_history import (
    get_context_history
)

from graph_builder.context_restore import (
    restore_context
)

history = get_context_history()

latest_context = history[-1]

result = restore_context(

    latest_context[
        "context_id"
    ]
)

print(
    "\nContext Restored\n"
)

pprint(
    result
)