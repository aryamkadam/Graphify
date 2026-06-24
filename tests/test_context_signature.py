from pprint import pprint

from graph_builder.universal_context_schema import (
    generate_universal_context_schema
)

from graph_builder.context_signature import (

    generate_context_signature,

    verify_context_signature
)

schema = (

    generate_universal_context_schema()
)

signature = (

    generate_context_signature(
        schema
    )
)

result = (

    verify_context_signature(

        schema,

        signature
    )
)

print(
    "\nContext Signature\n"
)

print(
    signature
)

print(
    "\nVerification\n"
)

pprint(
    result
)