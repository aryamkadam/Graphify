from pprint import pprint

from graph_builder.repository_metadata_exporter import (
    export_repository_metadata
)

metadata = (
    export_repository_metadata()
)

print()

print(
    "Repository Metadata Generated"
)

print()

pprint(
    metadata
)