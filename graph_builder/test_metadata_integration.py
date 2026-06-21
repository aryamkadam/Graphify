from pprint import pprint

from graph_builder.repository_metadata import (
    get_repository_metadata
)

metadata = get_repository_metadata()

pprint(metadata)