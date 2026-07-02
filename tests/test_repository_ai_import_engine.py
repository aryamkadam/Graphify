from pprint import pprint

from graph_builder.context.repository_ai_import_engine import (
    RepositoryAIImportEngine,
)

engine = RepositoryAIImportEngine()

print("\n========================================")
print("Repository AI Import Engine")
print("========================================\n")

result = engine.import_package(

    graphify_file="exports/repository_context.graphify",

    compressed_file="exports/repository_context.gctx",

)

pprint(result)