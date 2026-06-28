"""
Stage 16.2

Repository Reasoning Summary

Builds one executive summary from the
Repository Reasoning Engine.

Consumes the NEW reasoning object.

Repository Brain
        ↓
Repository Reasoning
        ↓
Executive Summary
"""

class RepositoryReasoningSummary:

   def build(self, reasoning):

        paragraphs = []

        purpose = reasoning.get(
            "repository_purpose"
        )

        if purpose:

            paragraphs.append(purpose)

        focus = reasoning.get(
            "current_focus"
        )

        if focus:

            paragraphs.append(

                f"Current engineering focus is {focus}."

            )

        risk = reasoning.get(
            "biggest_risk"
        )

        if risk:

            paragraphs.append(

                f"Biggest repository risk is {risk}."

            )

        critical = reasoning.get(
            "critical_module"
        )

        if critical != "Unknown":

            paragraphs.append(

                f"Critical repository component is {critical}."

            )

        next_step = reasoning.get(
            "recommended_next_step"
        )

        if next_step:

            paragraphs.append(

                f"Recommended next step is {next_step}."

            )

        story = reasoning.get(
            "repository_story"
        )

        if story:

            paragraphs.append(story)

        summary = " ".join(paragraphs)

        return {

            "summary": summary,

            "paragraphs": paragraphs

        }