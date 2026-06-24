from graph_builder.graphify_context_pack import (
    generate_graphify_context_pack
)

from graph_builder.graphify_pack_exporter import (
    export_graphify_pack
)

pack = (
    generate_graphify_context_pack()
)

path = (
    export_graphify_pack(
        pack
    )
)

print(
    "\nGraphify Pack Exported\n"
)

print(path)