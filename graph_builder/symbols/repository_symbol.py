"""
Graphify

Phase 11

Stage P11.4.1

Repository Symbol

Represents one engineering symbol extracted
from a repository.

This object is future-proof and can be
incrementally enriched by later phases.

Author:
Graphify Core
"""

from dataclasses import dataclass, field


@dataclass
class RepositorySymbol:

    VERSION = "P11.4.1"

    # --------------------------------------------------
    # Identity
    # --------------------------------------------------

    name: str

    symbol_type: str

    module: str

    line: int

    # --------------------------------------------------
    # Engineering Information
    # --------------------------------------------------

    arguments: list = field(default_factory=list)

    return_type: str | None = None

    decorators: list = field(default_factory=list)

    parent: str | None = None

    visibility: str = "PUBLIC"

    docstring: str | None = None

    # --------------------------------------------------

    def summary(self):

        return {

            "name": self.name,

            "type": self.symbol_type,

            "module": self.module,

            "version": self.VERSION,

        }

    # --------------------------------------------------

    def to_dict(self):

        return {

            "name": self.name,

            "symbol_type": self.symbol_type,

            "module": self.module,

            "line": self.line,

            "arguments": self.arguments,

            "return_type": self.return_type,

            "decorators": self.decorators,

            "parent": self.parent,

            "visibility": self.visibility,

            "docstring": self.docstring,

            "version": self.VERSION,

        }