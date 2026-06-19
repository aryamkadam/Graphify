from pathlib import Path

from parser.python_parser import parse_python_file
from graph_builder.builder import build_graph


def build_repository_graph(root_path):

    root = Path(root_path)

    node_ids = set()

    all_nodes = []
    all_edges = []

    file_registry = {}

    # First pass: build module registry
    for py_file in root.rglob("*.py"):

        if ".venv" in py_file.parts:
            continue

        if "__pycache__" in py_file.parts:
            continue

        module_name = str(
            py_file.relative_to(root)
        ).replace("\\", ".").replace(".py", "")

        file_registry[module_name] = str(
            py_file.relative_to(root)
        )

    # Second pass: build graph
    for py_file in root.rglob("*.py"):

        if ".venv" in py_file.parts:
            continue

        if "__pycache__" in py_file.parts:
            continue

        file_name = str(
            py_file.relative_to(root)
        )

        # File Node
        if file_name not in node_ids:

            node_ids.add(file_name)

            all_nodes.append(
                {
                    "id": file_name,
                    "type": "file"
                }
            )

        parsed_data = parse_python_file(
            py_file
        )

        graph = build_graph(
            parsed_data
        )

        # Import relationships
        for imported_module in parsed_data["imports"]:

            if imported_module in file_registry:

                all_edges.append(
                    {
                        "source": file_name,
                        "target": file_registry[
                            imported_module
                        ],
                        "type": "DEPENDS_ON"
                    }
                )

            else:

                all_edges.append(
                    {
                        "source": file_name,
                        "target": imported_module,
                        "type": "IMPORTS"
                    }
                )

        for node in graph["nodes"]:

            if node["id"] not in node_ids:

                node_ids.add(
                    node["id"]
                )

                all_nodes.append(
                    node
                )

            # File -> Node relationship
            all_edges.append(
                {
                    "source": file_name,
                    "target": node["id"],
                    "type": "CONTAINS"
                }
            )

        all_edges.extend(
            graph["edges"]
        )

    return {
        "nodes": all_nodes,
        "edges": all_edges
    }