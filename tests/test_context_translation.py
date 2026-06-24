from pprint import pprint

from graph_builder.cross_ai_transfer import (
    generate_cross_ai_transfer_pack
)

from graph_builder.context_translator import (
    translate_context_pack
)

pack = (

    generate_cross_ai_transfer_pack(

        "graphify-export/ctx_20260623201633878158.json"

    )

)

result = translate_context_pack(

    pack,

    "claude"

)

print(
    "\nTranslated Context Pack\n"
)

pprint(
    result
)