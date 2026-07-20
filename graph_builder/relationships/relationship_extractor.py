"""
Graphify

Phase 11

Stage P11.5.1

Relationship Extractor

Extracts engineering relationships
from a parsed PythonModule.

Architecture

RepositoryScanner
        ↓
RepositoryInventory

PythonASTParser
        ↓
PythonModule
        ↓
RelationshipExtractor

Author:
Graphify Core
"""

import ast

from graph_builder.parser.python_module import (
    PythonModule,
)

from graph_builder.relationships.repository_relationship import (
    RepositoryRelationship,
)


class RelationshipExtractor:

    VERSION = "P11.5.1"

    # --------------------------------------------------

    def extract(

        self,

        module: PythonModule,

    ):

        """
        Extract relationships from an already
        parsed PythonModule.

        No reparsing is performed.
        """

        relationships = []

        tree = module.ast_tree

        if tree is None:

            return relationships

        module_name = module.module_name

        # --------------------------------------------
        # Module Imports
        # --------------------------------------------

        for node in ast.walk(tree):

            if isinstance(node, ast.Import):

                for alias in node.names:

                    relationships.append(

                        RepositoryRelationship(

                            source=module_name,

                            relationship="IMPORTS",

                            target=alias.name,

                            module=module_name,

                            line=node.lineno,

                        )

                    )

            elif isinstance(node, ast.ImportFrom):

                if node.module is not None:

                    relationships.append(

                        RepositoryRelationship(

                            source=module_name,

                            relationship="IMPORTS",

                            target=node.module,

                            module=module_name,

                            line=node.lineno,

                        )

                    )

        # --------------------------------------------
        # Class Owns Function
        # --------------------------------------------

        for node in tree.body:

            if isinstance(node, ast.ClassDef):

                for child in node.body:

                    if isinstance(

                        child,

                        (

                            ast.FunctionDef,

                            ast.AsyncFunctionDef,

                        ),

                    ):

                        relationships.append(

                            RepositoryRelationship(

                                source=node.name,

                                relationship="OWNS",

                                target=child.name,

                                module=module_name,

                                line=child.lineno,

                            )

                        )

        return relationships