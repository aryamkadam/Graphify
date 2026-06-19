from graph_builder.module_dependency_map import (
    build_module_dependency_map
)

architecture = (
    build_module_dependency_map(".")
)

for module, info in sorted(
    architecture.items()
):

    print()

    print(
        f"MODULE: {module}"
    )

    print(
        f"File: {info['file']}"
    )

    print(
        f"Functions: {info['functions']}"
    )

    print(
        f"Classes: {info['classes']}"
    )

    print(
        f"Imports: {info['imports']}"
    )