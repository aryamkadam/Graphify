"""
Graphify

Phase 6

Stage P6.3

Dependency Graph Engine

Builds engineering dependency relationships
between planning work packages.

Author:
Graphify Core
"""


class DependencyGraphEngine:

    VERSION = "P6.3"

    # --------------------------------------------------

    def build(self, decomposition_report):

        packages = decomposition_report.get(

            "work_packages",

            [],

        )

        graph = {}

        previous = None

        for package in packages:

            graph[package] = {

                "depends_on": [] if previous is None else [previous]

            }

            previous = package

        return {

            "dependency_graph": graph,

            "nodes": len(packages),

            "edges": max(0, len(packages) - 1),

            "summary": (

                f"Dependency graph generated for "

                f"{len(packages)} work packages."

            ),

            "version": self.VERSION,

        }