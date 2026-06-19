from pathlib import Path

from parser.python_parser import (
    parse_python_file
)


def build_module_dependency_map(
    root_path
):

    root = Path(root_path)

    dependency_map = {}

    for py_file in root.rglob("*.py"):

        if ".venv" in py_file.parts:
            continue

        if "__pycache__" in py_file.parts:
            continue

        # Skip entire tests folder
        if "tests" in py_file.parts:
            continue

        relative_path = py_file.relative_to(
            root
        )

        module_name = (
            str(relative_path)
            .replace("\\", ".")
            .replace("/", ".")
            .removesuffix(".py")
        )

        parsed = parse_python_file(
            py_file
        )

        dependency_map[module_name] = {
            "file": str(relative_path),
            "functions": len(
                parsed["functions"]
            ),
            "classes": len(
                parsed["classes"]
            ),
            "imports": sorted(
                set(
                    parsed["imports"]
                )
            )
        }

    return dependency_map