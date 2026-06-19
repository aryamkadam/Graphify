from graph_builder.module_dependency_map import (
    build_module_dependency_map
)


def detect_architecture_layers(
    root_path
):

    modules = build_module_dependency_map(
        root_path
    )

    layers = {
        "presentation": [],
        "analysis": [],
        "knowledge": [],
        "data": [],
        "unknown": []
    }

    for module in modules:

        if module.startswith(
            "cli."
        ):

            layers[
                "presentation"
            ].append(module)

        elif module.startswith(
          ("parser.", "scanner.")
        ):

            layers[
                "analysis"
            ].append(module)

        elif module.startswith(
            "graph_builder."
        ):

            layers[
                "knowledge"
            ].append(module)

        elif "config" in module:

            layers[
                "data"
            ].append(module)

        else:

            layers[
                "unknown"
            ].append(module)

    return layers