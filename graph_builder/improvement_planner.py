def build_improvement_plan(
    recommendations
):

    plan = []

    for recommendation in recommendations:

        message = recommendation[
            "message"
        ]

        if (
            "dependency" in
            message.lower()
        ):

            plan.append(
                {
                    "priority":
                    recommendation[
                        "priority"
                    ],
                    "title":
                    "Reduce Coupling",
                    "steps": [
                        "Identify dependent modules.",
                        "Extract shared logic.",
                        "Create reusable utilities.",
                        "Reduce direct dependencies."
                    ]
                }
            )

        elif (
            "high-risk" in
            message.lower()
        ):

            plan.append(
                {
                    "priority":
                    recommendation[
                        "priority"
                    ],
                    "title":
                    "Review Risky Symbol",
                    "steps": [
                        "Inspect implementation.",
                        "Add tests.",
                        "Review callers.",
                        "Refactor if needed."
                    ]
                }
            )

        elif (
            "splitting" in
            message.lower()
        ):

            plan.append(
                {
                    "priority":
                    recommendation[
                        "priority"
                    ],
                    "title":
                    "Split Large File",
                    "steps": [
                        "Identify responsibilities.",
                        "Create new modules.",
                        "Move related functions.",
                        "Update imports."
                    ]
                }
            )

        elif (
            "dead symbols" in
            message.lower()
        ):

            plan.append(
                {
                    "priority":
                    recommendation[
                        "priority"
                    ],
                    "title":
                    "Clean Dead Code",
                    "steps": [
                        "Verify unused symbols.",
                        "Remove obsolete code.",
                        "Run tests.",
                        "Commit cleanup."
                    ]
                }
            )

    return plan