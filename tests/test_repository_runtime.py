from pprint import pprint

from graph_builder.runtime.repository_runtime import RepositoryRuntime

runtime = RepositoryRuntime()

print("\n========================================")
print("Repository Runtime")
print("========================================\n")

pprint(runtime.status())

print("\nBoot Runtime\n")

runtime.boot()

pprint(runtime.status())

print("\nRuntime Online\n")

runtime.online()

pprint(runtime.status())