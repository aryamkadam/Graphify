from pprint import pprint

from graph_builder.schema_versioning import (

    get_schema_version,

    check_schema_compatibility
)

print(
    "\nCurrent Schema Version\n"
)

print(
    get_schema_version()
)

print(
    "\nCompatibility Test\n"
)

pprint(

    check_schema_compatibility(
        "1.0"
    )
)

pprint(

    check_schema_compatibility(
        "1.1"
    )
)

pprint(

    check_schema_compatibility(
        "2.0"
    )
)