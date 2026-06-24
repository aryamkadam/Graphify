from pprint import pprint

from graph_builder.cross_ai_transfer import (
    generate_cross_ai_transfer_pack
)

result = (

    generate_cross_ai_transfer_pack(

        "graphify-export/ctx_20260623201633878158.json"

    )

)

print(
    "\nCross AI Transfer Pack Generated\n"
)

pprint(
    result
)