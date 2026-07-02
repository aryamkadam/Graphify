from pprint import pprint

from graph_builder.context.repository_export_manifest import (
    RepositoryExportManifest,
)

builder = RepositoryExportManifest()

print("\n========================================")
print("Repository Export Manifest")
print("========================================\n")

manifest = builder.build(

    target_ai="chatgpt",

)

pprint(manifest)