from pprint import pprint

from graph_builder.cross_ai_transfer import (
    generate_cross_ai_transfer_pack
)

from graph_builder.context_translator_v2 import (
    translate_context_pack_v2
)

pack = (

    generate_cross_ai_transfer_pack(

        "graphify-export/ctx_20260623201633878158.json"

    )

)

print(
    "\nClaude Translation\n"
)

pprint(

    translate_context_pack_v2(

        pack,

        "claude"

    )

)

print(
    "\nGemini Translation\n"
)

pprint(

    translate_context_pack_v2(

        pack,

        "gemini"

    )

)

print(
    "\nLocal LLM Translation\n"
)

pprint(

    translate_context_pack_v2(

        pack,

        "local"

    )

)