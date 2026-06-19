import ast


def extract_parameters(node):

    params = []

    for arg in node.args.args:

        params.append(
            arg.arg
        )

    return params


def parse_python_file(file_path):

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as f:

        source = f.read()

    tree = ast.parse(source)

    functions = []
    classes = []
    imports = []
    calls = []

    for node in ast.walk(tree):

        if isinstance(node, ast.FunctionDef):

            functions.append(
                {
                    "name": node.name,
                    "line": node.lineno,
                    "parameters": extract_parameters(node),
                    "docstring": ast.get_docstring(node)
                }
            )

            for child in ast.walk(node):

                if isinstance(child, ast.Call):

                    if isinstance(
                        child.func,
                        ast.Name
                    ):

                        calls.append(
                            {
                                "caller": node.name,
                                "callee": child.func.id
                            }
                        )

        elif isinstance(node, ast.ClassDef):

            classes.append(
                {
                    "name": node.name,
                    "line": node.lineno,
                    "docstring": ast.get_docstring(node)
                }
            )

        elif isinstance(node, ast.Import):

            for alias in node.names:

                imports.append(
                    alias.name
                )

        elif isinstance(node, ast.ImportFrom):

            if node.module:

                imports.append(
                    node.module
                )

    return {
        "functions": functions,
        "classes": classes,
        "imports": imports,
        "calls": calls
    }