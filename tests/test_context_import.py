from pprint import pprint

from graph_builder.context_importer import (
    import_context_pack
)

from graph_builder.context_import_summary import (
    generate_import_summary
)

file_path = (
    "graphify-export/"
    "ctx_20260623201633878158.json"
)

context = import_context_pack(
    file_path
)

summary = generate_import_summary(
    context
)

print(
    "\nContext Imported\n"
)

pprint(
    summary
)