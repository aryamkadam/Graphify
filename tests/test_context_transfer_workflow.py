from pprint import pprint

from graph_builder.context_transfer_workflow import (
    execute_context_transfer
)

result = (
    execute_context_transfer()
)

print(
    "\nGRAPHIFY CONTEXT TRANSFER\n"
)

pprint(result)