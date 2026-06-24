from graph_builder.context_importer import (
    import_context_pack
)

from graph_builder.context_bootstrap import (
    generate_context_bootstrap
)

context = import_context_pack(
    "graphify-export/ctx_20260623201633878158.json"
)

result = generate_context_bootstrap(
    context
)

print(
    "\nDynamic Bootstrap Generated\n"
)

print(
    result
)