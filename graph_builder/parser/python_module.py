"""
Graphify

Phase 11

Stage P11.3.1

Python Module

Represents a parsed Python file.

Contains repository facts and the parsed AST.

Author:
Graphify Core
"""

from dataclasses import dataclass, field
import ast


@dataclass
class PythonModule:

    VERSION = "P11.3.1"

    module_name: str

    file_path: str

    # --------------------------------------------------
    # Persistent AST
    # --------------------------------------------------

    ast_tree: ast.Module | None = None

    # --------------------------------------------------

    imports: list = field(default_factory=list)

    classes: list = field(default_factory=list)

    functions: list = field(default_factory=list)

    async_functions: list = field(default_factory=list)

    docstring: str | None = None

    line_count: int = 0

    # --------------------------------------------------

    def summary(self):

        return {

            "module": self.module_name,

            "imports": len(self.imports),

            "classes": len(self.classes),

            "functions": len(self.functions),

            "async_functions": len(self.async_functions),

            "version": self.VERSION,

        }

    # --------------------------------------------------

    def to_dict(self):

        return {

            "module_name": self.module_name,

            "file_path": self.file_path,

            "imports": self.imports,

            "classes": self.classes,

            "functions": self.functions,

            "async_functions": self.async_functions,

            "docstring": self.docstring,

            "line_count": self.line_count,

            "version": self.VERSION,

        }