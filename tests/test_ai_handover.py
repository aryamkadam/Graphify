from pprint import pprint

from graph_builder.context_importer import (
    import_context_pack
)

from graph_builder.ai_handover import (
    generate_ai_handover
)

context = import_context_pack(
    "graphify-export/ctx_20260623201633878158.json"
)

handover = generate_ai_handover(
    context
)

print(
    "\nAI Handover Generated\n"
)

pprint(
    handover
)