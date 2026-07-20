"""
Graphify

Phase 11

Stage P11.7.1

Repository Architecture Diagnostic Engine

Converts architecture validation into
engineering diagnostics.

Author:
Graphify Core
"""

from datetime import datetime


class RepositoryArchitectureDiagnosticEngine:

    VERSION = "P11.7.1"

    def diagnose(self, validation_report):

        diagnostics = []

        issue_counter = 1

        # ----------------------------------------
        # Duplicate Responsibilities
        # ----------------------------------------

        for duplicate in validation_report.get(
            "duplicate_responsibilities",
            [],
        ):

            diagnostics.append(
                {
                    "issue_id": f"ARCH-{issue_counter:03}",
                    "category": "Duplicate Responsibility",
                    "severity": self._duplicate_severity(
                        duplicate["occurrences"]
                    ),
                    "affected_components": duplicate["paths"],
                    "reason": (
                        f"{duplicate['component']} appears "
                        f"{duplicate['occurrences']} times."
                    ),
                    "engineering_risk": (
                        "Multiple implementations may diverge over time."
                    ),
                    "recommended_fix": (
                        f"Centralize '{duplicate['component']}' into a "
                        "single engineering owner."
                    ),
                    "confidence": 0.98,
                }
            )

            issue_counter += 1

        # ----------------------------------------
        # Oversized Layers
        # ----------------------------------------

        for layer in validation_report.get(
            "oversized_layers",
            [],
        ):

            diagnostics.append(
                {
                    "issue_id": f"ARCH-{issue_counter:03}",
                    "category": "Oversized Layer",
                    "severity": self._layer_severity(
                        layer["components"]
                    ),
                    "affected_components": [layer["layer"]],
                    "reason": (
                        f"{layer['layer']} contains "
                        f"{layer['components']} components."
                    ),
                    "engineering_risk": (
                        "Large layers reduce maintainability."
                    ),
                    "recommended_fix": (
                        "Split layer into smaller domains."
                    ),
                    "confidence": 0.95,
                }
            )

            issue_counter += 1

        # ----------------------------------------
        # Architecture Cycles
        # ----------------------------------------

        for cycle in validation_report.get(
            "architecture_cycles",
            [],
        ):

            diagnostics.append(
                {
                    "issue_id": f"ARCH-{issue_counter:03}",
                    "category": "Architecture Cycle",
                    "severity": "CRITICAL",
                    "affected_components": cycle,
                    "reason": (
                        "Circular dependency detected."
                    ),
                    "engineering_risk": (
                        "Architecture becomes difficult to evolve."
                    ),
                    "recommended_fix": (
                        "Break circular dependency using abstraction."
                    ),
                    "confidence": 1.0,
                }
            )

            issue_counter += 1

        return {
            "repository": validation_report.get(
                "repository",
                "",
            ),
            "generated_at": datetime.utcnow().isoformat() + "Z",
            "version": self.VERSION,
            "total_issues": len(diagnostics),
            "engineering_risk": self._overall_risk(
                diagnostics
            ),
            "diagnostics": diagnostics,
        }

    # ----------------------------------------

    def _duplicate_severity(self, occurrences):

        if occurrences >= 5:
            return "CRITICAL"

        if occurrences >= 3:
            return "HIGH"

        return "MEDIUM"

    # ----------------------------------------

    def _layer_severity(self, components):

        if components >= 300:
            return "CRITICAL"

        if components >= 150:
            return "HIGH"

        return "MEDIUM"

    # ----------------------------------------

    def _overall_risk(self, diagnostics):

        if not diagnostics:
            return "LOW"

        severities = [
            d["severity"]
            for d in diagnostics
        ]

        if "CRITICAL" in severities:
            return "CRITICAL"

        if "HIGH" in severities:
            return "HIGH"

        if "MEDIUM" in severities:
            return "MEDIUM"

        return "LOW"