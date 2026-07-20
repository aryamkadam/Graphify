"""
Graphify

Phase 11

Stage P11.7

Repository Architecture Validator

Validates whether the repository still
follows Graphify's engineering architecture.

Author:
Graphify Core
"""

from collections import defaultdict

from graph_builder.architecture.repository_architecture_report import (
    RepositoryArchitectureReport,
)


class RepositoryArchitectureValidator:

    VERSION = "P11.7"

    # --------------------------------------------------

    def validate(

        self,

        architecture_index,

    ):

        components = architecture_index["components"]

        duplicates = self._duplicate_responsibilities(

            components,

        )

        oversized = self._oversized_layers(

            architecture_index["layer_summary"],

        )

        cycles = []

        recommendations = self._recommendations(

            duplicates,

            oversized,

        )

        health = self._health_score(

            duplicates,

            oversized,

            cycles,

        )

        report = RepositoryArchitectureReport(

            repository=

                architecture_index["repository"],

            health_score=health,

            duplicate_responsibilities=duplicates,

            oversized_layers=oversized,

            architecture_cycles=cycles,

            recommendations=recommendations,

        )

        return report.export()

    # --------------------------------------------------

    def _duplicate_responsibilities(

        self,

        components,

    ):

        grouped = defaultdict(list)

        duplicates = []

        for component in components:

            grouped[component.name].append(component.path)

        for name, paths in grouped.items():

            if len(paths) > 1:

                duplicates.append(

                    {

                        "component": name,

                        "occurrences": len(paths),

                        "paths": paths,

                    }

                )

        return duplicates

    # --------------------------------------------------

    def _oversized_layers(

        self,

        layer_summary,

    ):

        oversized = []

        for layer, count in layer_summary.items():

            if count > 50:

                oversized.append(

                    {

                        "layer": layer,

                        "components": count,

                    }

                )

        return oversized

    # --------------------------------------------------

    def _recommendations(

        self,

        duplicates,

        oversized,

    ):

        recommendations = []

        if duplicates:

            recommendations.append(

                "Review duplicated engineering responsibilities."

            )

        if oversized:

            recommendations.append(

                "Split oversized architectural layers."

            )

        if not recommendations:

            recommendations.append(

                "Architecture follows canonical structure."

            )

        return recommendations

    # --------------------------------------------------

    def _health_score(

        self,

        duplicates,

        oversized,

        cycles,

    ):

        score = 100

        score -= len(duplicates) * 5

        score -= len(oversized) * 3

        score -= len(cycles) * 10

        return max(score, 0)