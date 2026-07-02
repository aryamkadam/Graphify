from pprint import pprint

from graph_builder.context.repository_transfer_package import (
    RepositoryTransferPackage,
)

builder = RepositoryTransferPackage()

print("\n========================================")
print("Repository Transfer Package")
print("========================================\n")

result = builder.build(

    serialized_file="exports/repository_context.graphify",

    compressed_file="exports/repository_context.gctx",

    target_ai="chatgpt",

)

pprint(result)