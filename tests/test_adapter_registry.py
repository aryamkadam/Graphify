from pprint import pprint

from graph_builder.protocols.uacp.adapters.registry import (

    available_adapters,

    get_adapter

)

print()

print("Registered Adapters")

print()

pprint(

    available_adapters()

)

print()

adapter = get_adapter(

    "chatgpt"

)

print(

    adapter.__name__

)