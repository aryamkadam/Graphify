

from pprint import pprint

from graph_builder.universal_context_schema import (
    generate_universal_context_schema
)

from graph_builder.context_schema_validator import (
    validate_context_schema
)

schema = (
    generate_universal_context_schema()
)

result = (
    validate_context_schema(
        schema
    )
)

print(
    "\nContext Schema Validation\n"
)

pprint(
    result
)