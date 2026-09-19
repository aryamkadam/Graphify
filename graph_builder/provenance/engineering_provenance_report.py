"""
Graphify

Phase 38
Stage 38.7

Engineering Provenance Report

Presentation-only projection of an existing
EngineeringDecisionRecord.

This component does not create decisions, plans, policy,
memory, execute engineering work, mutate repositories,
or infer unsupported engineering facts.

Author:
Graphify Core
"""

from __future__ import annotations


class EngineeringProvenanceReport:

    VERSION = "38.7"

    def build(
        self,
        record,
    ):
        """
        Build a human-readable engineering provenance report
        from an existing EngineeringDecisionRecord.
        """

        if not isinstance(
            record,
            dict,
        ):
            raise TypeError(
                "record must be a dictionary."
            )

        decision = (
            record.get(
                "decision",
                {},
            )
            or {}
        )

        plan = (
            record.get(
                "plan",
                {},
            )
            or {}
        )

        evidence = (
            record.get(
                "evidence",
                {},
            )
            or {}
        )

        knowledge = (
            record.get(
                "knowledge",
                {},
            )
            or {}
        )

        unknowns = (
            record.get(
                "unknowns",
                [],
            )
            or []
        )

        repository = record.get(
            "repository",
            "UNKNOWN",
        )

        lines = [

            "# Graphify Engineering Provenance Report",

            "",

            f"Repository: {repository}",

            "",

            "## Current Engineering Decision",

            self._value(
                "Selected Goal",
                decision.get(
                    "selected_goal"
                ),
            ),

            self._value(
                "Decision",
                decision.get(
                    "decision"
                ),
            ),

            self._value(
                "Decision Rationale",
                knowledge.get(
                    "decision_rationale",
                    "UNKNOWN",
                ),
            ),

            self._value(
                "Strategic Focus",
                decision.get(
                    "strategic_focus"
                ),
            ),

            self._value(
                "Policy Action",
                decision.get(
                    "policy_action"
                ),
            ),

            "",

            "## Current Plan",

            self._value(
                "Objective",
                plan.get(
                    "objective"
                ),
            ),

            self._value(
                "Engineering Strategy",
                plan.get(
                    "engineering_strategy"
                ),
            ),

            self._value(
                "Expected Result",
                plan.get(
                    "expected_result"
                ),
            ),

            "",

            "## Next Planned Engineering Task",

            self._next_task(
                plan
            ),

            "",

            "## Direct Evidence",

        ]

        lines.extend(
            self._evidence_lines(
                evidence.get(
                    "direct",
                    [],
                )
            )
        )

        lines.extend([

            "",

            "## Related Evidence",

        ])

        lines.extend(
            self._evidence_lines(
                evidence.get(
                    "related",
                    [],
                )
            )
        )

        lines.extend([

            "",

            "## Context Evidence",

        ])

        lines.extend(
            self._evidence_lines(
                evidence.get(
                    "context",
                    [],
                )
            )
        )

        lines.extend([

            "",

            "## Knowledge Status",

        ])

        lines.append(
            self._value(
                "Outcome",
                knowledge.get(
                    "outcome",
                    "UNKNOWN",
                ),
            )
        )

        lines.append(
            self._value(
                "Decision Validity",
                knowledge.get(
                    "decision_validity",
                    "UNKNOWN",
                ),
            )
        )

        lines.append(
            self._value(
                "Decision Confidence",
                knowledge.get(
                    "decision_confidence",
                    "UNKNOWN",
                ),
            )
        )

        counts = (
            evidence.get(
                "counts",
                {},
            )
            or {}
        )

        lines.extend([

            "",

            "Evidence Counts",

            f"- Direct: {counts.get('direct', 0)}",

            f"- Related: {counts.get('related', 0)}",

            f"- Context: {counts.get('context', 0)}",

            f"- Unknown: {counts.get('unknown', 0)}",

        ])

        lines.extend([

            "",

            "## Unknown / Missing Evidence",

        ])

        if unknowns:

            for item in unknowns:

                lines.append(
                    f"- {item}"
                )

        else:

            lines.append(
                "- None reported."
            )

        lines.extend([

            "",

            "## Trust Boundary",

            "- Repository evidence is observational.",

            "- Correlation is not treated as causality.",

            "- Unsupported rationale remains UNKNOWN.",

            "- Unsupported outcomes remain UNKNOWN.",

            "- This report does not create engineering decisions.",

            "- This report does not create engineering plans.",

            "- This report does not execute repository work.",

            "",

            "## Provenance",

            "- Decision authority: RepositoryDecisionEngine",

            "- Policy authority: RepositoryDecisionPolicy",

            "- Planning authority: RepositoryExecutionPlanningEngine",

            "- Experience authority: EngineeringMemory",

            "- Evidence collector: DecisionEvidenceCollector",

            "- Report layer: EngineeringProvenanceReport",

        ])

        return "\n".join(
            lines
        )

    @staticmethod
    def _value(
        label,
        value,
    ):

        if value is None:
            value = "UNKNOWN"

        return (
            f"**{label}:** {value}"
        )

    @staticmethod
    def _next_task(
        plan,
    ):

        if not isinstance(
            plan,
            dict,
        ):
            return "UNKNOWN"

        for sprint in (
            plan.get(
                "sprints",
                [],
            )
            or []
        ):

            if not isinstance(
                sprint,
                dict,
            ):
                continue

            for task in (
                sprint.get(
                    "tasks",
                    [],
                )
                or []
            ):

                if (
                    isinstance(
                        task,
                        str,
                    )
                    and task.strip()
                ):

                    return task.strip()

        return "UNKNOWN"

    @staticmethod
    def _evidence_lines(
        items,
    ):

        lines = []

        if not items:

            return [
                "- None found."
            ]

        for item in items:

            if not isinstance(
                item,
                dict,
            ):
                continue

            evidence_type = item.get(
                "type",
                "repository_evidence",
            )

            path = item.get(
                "path"
            )

            commit = item.get(
                "commit"
            )

            message = item.get(
                "message"
            )

            if path:

                description = (
                    f"{evidence_type}: `{path}`"
                )

            elif commit:

                description = (
                    f"{evidence_type}: `{commit}`"
                )

            else:

                description = evidence_type

            if message:

                description += (
                    f" — {message}"
                )

            lines.append(
                f"- {description}"
            )

        if not lines:

            lines.append(
                "- None found."
            )

        return lines
