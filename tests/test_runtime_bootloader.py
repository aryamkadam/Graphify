from pprint import pprint

from graph_builder.runtime.repository_runtime import RepositoryRuntime

runtime = RepositoryRuntime()

print("\n========================================")
print("Runtime Bootloader")
print("========================================\n")

result = runtime.boot_repository(

    "graphify_export",

)

pprint(result)

print("\nRuntime Status\n")

pprint(runtime.status())