from pathlib import Path

from parser.python_parser import (
    parse_python_file
)


def generate_repository_summary(
    root_path
):

    root = Path(root_path)

    total_files = 0
    total_functions = 0
    total_classes = 0

    modules = set()

    for py_file in root.rglob("*.py"):

        if ".venv" in py_file.parts:
            continue

        if "__pycache__" in py_file.parts:
            continue

        total_files += 1

        parsed = parse_python_file(
            py_file
        )

        total_functions += len(
            parsed["functions"]
        )

        total_classes += len(
            parsed["classes"]
        )

        if len(py_file.parts) > 1:

            modules.add(
                py_file.parts[0]
            )

    return {
        "project_name": root.resolve().name,
        "total_files": total_files,
        "total_functions": total_functions,
        "total_classes": total_classes,
        "total_modules": len(modules),
        "modules": sorted(
            list(modules)
        )
    }