"""
Graphify

Phase 11

Stage P11.6.1

Repository Architecture Index

Builds the structural understanding of the
repository.

This is NOT just an index.

It is the first step toward Graphify
understanding its own architecture.

Author:
Graphify Core
"""

from pathlib import Path

from graph_builder.architecture.architecture_component import (
    ArchitectureComponent,
)

from graph_builder.architecture.architecture_layer import (
    CANONICAL_LAYERS,
)


class RepositoryArchitectureIndex:

    VERSION = "P11.6.1"

    _IGNORE = {

        ".git",
        ".venv",
        "__pycache__",
        ".pytest_cache",
        "build",
        "dist",
        ".idea",
        ".vscode",
        "node_modules",

    }

    # -----------------------------------------------------

    def build(

        self,

        repository_root: str,

    ):

        root = Path(repository_root).resolve()

        components = []

        layer_summary = {}

        for py_file in root.rglob("*.py"):

            relative = py_file.relative_to(root)

            # ---------------------------------------------
            # Ignore non-engineering folders
            # ---------------------------------------------

            if any(

                part in self._IGNORE

                for part in relative.parts

            ):

                continue

            layer = self._detect_layer(

                relative.parts,

            )

            role = self._detect_role(

                py_file.stem,

            )

            importance = self._importance(

                role,

            )

            visibility = (

                "PRIVATE"

                if py_file.stem.startswith("_")

                else "PUBLIC"

            )

            component = ArchitectureComponent(

                name=py_file.stem,

                path=str(relative),

                module=".".join(

                    relative.with_suffix("").parts

                ),

                layer=layer,

                role=role,

                visibility=visibility,

                symbol_count=0,

                relationship_count=0,

                importance=importance,

            )

            components.append(component)

            layer_summary[layer] = (

                layer_summary.get(layer, 0) + 1

            )

        return {

            "repository": root.name,

            "component_count": len(components),

            "layer_summary": dict(

                sorted(layer_summary.items())

            ),

            "components": components,

            "version": self.VERSION,

        }

    # -----------------------------------------------------

    def _detect_layer(

        self,

        relative_parts,

    ):

        if (

            len(relative_parts) >= 2

            and relative_parts[0] == "graph_builder"

        ):

            return CANONICAL_LAYERS.get(

                relative_parts[1],

                "Infrastructure",

            )

        if relative_parts[0] == "tests":

            return "Tests"

        if relative_parts[0] == "docs":

            return "Documentation"

        if relative_parts[0] == "cli":

            return "CLI"

        return "Infrastructure"

    # -----------------------------------------------------

    def _detect_role(

        self,

        filename,

    ):

        filename = filename.lower()

        if "brain" in filename:

            return "BRAIN"

        if "engine" in filename:

            return "ENGINE"

        if "worker" in filename:

            return "WORKER"

        if "parser" in filename:

            return "PARSER"

        if "knowledge" in filename:

            return "KNOWLEDGE"

        if "runtime" in filename:

            return "RUNTIME"

        if "graph" in filename:

            return "GRAPH"

        if "memory" in filename:

            return "MEMORY"

        if "planner" in filename:

            return "PLANNER"

        if "decision" in filename:

            return "DECISION"

        if "repository" in filename:

            return "REPOSITORY"

        return "UTILITY"

    # -----------------------------------------------------

    def _importance(

        self,

        role,

    ):

        if role == "BRAIN":

            return "CRITICAL"

        if role in {

            "ENGINE",
            "KNOWLEDGE",
            "RUNTIME",
            "WORKER",
            "PLANNER",
            "DECISION",

        }:

            return "HIGH"

        if role in {

            "PARSER",
            "GRAPH",
            "MEMORY",

        }:

            return "MEDIUM"

        return "NORMAL"