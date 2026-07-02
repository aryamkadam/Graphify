from pprint import pprint

from graph_builder.context.repository_package_verifier import (
    RepositoryPackageVerifier,
)

verifier = RepositoryPackageVerifier()

print("\n========================================")
print("Repository Package Verifier")
print("========================================\n")

result = verifier.verify(

    "graphify_export",

)

pprint(result)