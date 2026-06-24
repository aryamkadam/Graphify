from pprint import pprint

from graph_builder.graphify_context_pack import (
    generate_graphify_context_pack
)

pack = (
    generate_graphify_context_pack()
)

print(
    "\nGRAPHIFY CONTEXT PACK V1\n"
)

pprint(pack)