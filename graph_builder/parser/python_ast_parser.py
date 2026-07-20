"""
Graphify

Phase 11

Stage P11.3.1

Python AST Parser

Parses Python source into structured engineering facts.

Persists the AST for downstream engineering
components.

Author:
Graphify Core
"""

import ast
from pathlib import Path

from graph_builder.parser.python_module import PythonModule


class PythonASTParser:

    VERSION = "P11.3.1"

    # --------------------------------------------------

    def parse(self, file_path):

        path = Path(file_path)

        source = path.read_text(

            encoding="utf-8"

        )

        tree = ast.parse(source)

        # ----------------------------------------------
        # Build PythonModule
        # ----------------------------------------------

        module = PythonModule(

            module_name=path.stem,

            file_path=str(path),

            ast_tree=tree,

        )

        module.docstring = ast.get_docstring(tree)

        module.line_count = len(

            source.splitlines()

        )

        # ----------------------------------------------
        # Collect engineering facts
        # ----------------------------------------------

        for node in ast.walk(tree):

            if isinstance(node, ast.Import):

                for alias in node.names:

                    module.imports.append(

                        alias.name

                    )

            elif isinstance(node, ast.ImportFrom):

                if node.module:

                    module.imports.append(

                        node.module

                    )

            elif isinstance(node, ast.ClassDef):

                module.classes.append(

                    node.name

                )

            elif isinstance(node, ast.FunctionDef):

                module.functions.append(

                    node.name

                )

            elif isinstance(node, ast.AsyncFunctionDef):

                module.async_functions.append(

                    node.name

                )

        return module