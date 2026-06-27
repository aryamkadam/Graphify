"""
Stage 15.7.3

Repository Reasoning Summary

Converts repository reasoning into one
high-level engineering assessment.

This summary is designed for:

- AI Assistants
- CTO Dashboards
- Repository Brain
- Executive Reports
"""

class RepositoryReasoningSummary:

    def generate(self, reasoning):

        health = reasoning.get("health_reasoning", [])

        execution = reasoning.get("execution_reasoning", [])

        knowledge = reasoning.get("knowledge_reasoning", [])

        decision = reasoning.get("decision_reasoning", [])

        direction = reasoning.get("repository_direction", [])

        paragraphs = []

        # ----------------------------------

        if health:

            paragraphs.append(
                "Repository health analysis indicates that "
                + health[0].lower()
            )

        # ----------------------------------

        if execution:

            paragraphs.append(
                "Execution analysis shows that "
                + execution[0].lower()
            )

        # ----------------------------------

        if knowledge:

            paragraphs.append(
                "Knowledge analysis suggests that "
                + knowledge[0].lower()
            )

        # ----------------------------------

        if decision:

            paragraphs.append(
                "Decision history demonstrates that "
                + decision[0].lower()
            )

        # ----------------------------------

        if direction:

            paragraphs.append(
                direction[0]
            )

        summary = " ".join(paragraphs)

        return {

            "summary": summary,

            "paragraphs": paragraphs

        }