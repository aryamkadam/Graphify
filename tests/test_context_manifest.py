from pprint import pprint

from graph_builder.context_manifest import (
    generate_context_manifest
)

manifest = (
    generate_context_manifest()
)

print(
    "\nContext Manifest Generated\n"
)

pprint(
    manifest
)