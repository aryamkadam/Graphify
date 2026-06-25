from pprint import pprint

from graph_builder.graphify_context_pack import (
    generate_graphify_context_pack
)

from graph_builder.context_pack_verifier import (
    verify_context_pack
)

pack = (
    generate_graphify_context_pack()
)

result = (
    verify_context_pack(
        pack
    )
)

print(
    "\nContext Pack Verification\n"
)

pprint(result)