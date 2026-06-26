from pprint import pprint

from graph_builder.protocols.uacp.protocol import (
    create_protocol
)

from graph_builder.protocols.uacp.serializer import (

    serialize_uacp_json,

    save_uacp_json,

    load_uacp_json

)

protocol = create_protocol()

print()

print("UACP Serialization")

print()

json_text = serialize_uacp_json(
    protocol
)

print(json_text[:250])

print()

save_uacp_json(

    protocol,

    "uacp.json"

)

loaded = load_uacp_json(
    "uacp.json"
)

print("Loaded")

print()

pprint(

    loaded["protocol"]

)