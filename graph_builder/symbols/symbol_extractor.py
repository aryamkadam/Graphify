"""
Graphify

Phase 11

Stage P11.4.2

Symbol Extractor

Extracts engineering symbols from a parsed PythonModule.

Architecture

RepositoryScanner
        ↓
RepositoryInventory

PythonASTParser
        ↓
PythonModule
        ↓
SymbolExtractor

Author:
Graphify Core
"""

import ast

from graph_builder.symbols.repository_symbol import (
    RepositorySymbol,
)

from graph_builder.parser.python_module import (
    PythonModule,
)


class SymbolExtractor:

    VERSION = "P11.4.2"

    # --------------------------------------------------

    def extract(

        self,

        module: PythonModule,

    ):

        """
        Extract engineering symbols from an
        already parsed PythonModule.

        No reparsing is performed.
        """

        symbols = []

        tree = module.ast_tree

        if tree is None:

            return symbols

        module_name = module.module_name

        # ----------------------------------------------
        # Walk AST
        # ----------------------------------------------

        for node in ast.walk(tree):

            # ------------------------------------------
            # Classes
            # ------------------------------------------

            if isinstance(node, ast.ClassDef):

                symbols.append(

                    RepositorySymbol(

                        name=node.name,

                        symbol_type="CLASS",

                        module=module_name,

                        line=node.lineno,

                        arguments=[],

                        decorators=[

                            ast.unparse(decorator)

                            for decorator in node.decorator_list

                        ],

                        docstring=ast.get_docstring(node),

                    )

                )

            # ------------------------------------------
            # Functions
            # ------------------------------------------

            elif isinstance(node, ast.FunctionDef):

                symbols.append(

                    RepositorySymbol(

                        name=node.name,

                        symbol_type="FUNCTION",

                        module=module_name,

                        line=node.lineno,

                        arguments=[

                            argument.arg

                            for argument in node.args.args

                        ],

                        decorators=[

                            ast.unparse(decorator)

                            for decorator in node.decorator_list

                        ],

                        docstring=ast.get_docstring(node),

                    )

                )

            # ------------------------------------------
            # Async Functions
            # ------------------------------------------

            elif isinstance(node, ast.AsyncFunctionDef):

                symbols.append(

                    RepositorySymbol(

                        name=node.name,

                        symbol_type="ASYNC_FUNCTION",

                        module=module_name,

                        line=node.lineno,

                        arguments=[

                            argument.arg

                            for argument in node.args.args

                        ],

                        decorators=[

                            ast.unparse(decorator)

                            for decorator in node.decorator_list

                        ],

                        docstring=ast.get_docstring(node),

                    )

                )

        return symbols