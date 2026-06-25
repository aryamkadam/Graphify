from pprint import pprint

from graph_builder.graphify_pack_importer import (
    import_graphify_pack
)

pack = (
    import_graphify_pack()
)

print(
    "\nGraphify Pack Imported\n"
)

pprint(pack)