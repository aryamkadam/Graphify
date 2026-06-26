from pprint import pprint

from graph_builder.protocols.uacp.protocol import (
    create_protocol
)

from graph_builder.protocols.uacp.validator import (
    validate_uacp
)

protocol = create_protocol()

print()

print("UACP Validation")

print()

pprint(

    validate_uacp(
        protocol
    )

)