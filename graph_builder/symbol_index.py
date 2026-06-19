from pathlib import Path

from parser.python_parser import parse_python_file


def build_symbol_index(root_path):

    root = Path(root_path)

    symbols = {}

    # PASS 1: Build symbol database
    for py_file in root.rglob("*.py"):

        if ".venv" in py_file.parts:
            continue

        if "__pycache__" in py_file.parts:
            continue

        if py_file.parent.name == "tests":
            continue

        if py_file.name.startswith("test_"):
            continue

        if py_file.name == "test.py":
            continue

        parsed = parse_python_file(
            py_file
        )

        relative_path = str(
            py_file.relative_to(root)
        )

        for function in parsed["functions"]:

            symbols[
                function["name"]
            ] = {
                "file": relative_path,
                "type": "function",
                "line": function["line"],
                "parameters": function["parameters"],
                "docstring": function["docstring"],
                "used_by": []
            }

        for cls in parsed["classes"]:

            symbols[
                cls["name"]
            ] = {
                "file": relative_path,
                "type": "class",
                "line": cls["line"],
                "docstring": cls["docstring"],
                "used_by": []
            }

    # PASS 2: Resolve usages
    for py_file in root.rglob("*.py"):

        if ".venv" in py_file.parts:
            continue

        if "__pycache__" in py_file.parts:
            continue

        if py_file.parent.name == "tests":
            continue

        if py_file.name.startswith("test_"):
            continue

        if py_file.name == "test.py":
            continue

        parsed = parse_python_file(
            py_file
        )

        relative_path = str(
            py_file.relative_to(root)
        )

        for call in parsed["calls"]:

            callee = call["callee"]

            if callee in symbols:

                existing = None

                for usage in symbols[
                    callee
                ]["used_by"]:

                    if (
                        usage["file"]
                        == relative_path
                        and
                        usage["caller"]
                        == call["caller"]
                    ):

                        existing = usage
                        break

                if existing:

                    existing["count"] += 1

                else:

                    symbols[
                        callee
                    ]["used_by"].append(
                        {
                            "file": relative_path,
                            "caller": call["caller"],
                            "count": 1
                        }
                    )

    return symbols