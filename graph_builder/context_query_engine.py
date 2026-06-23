def query_context(
    context,
    question
):

    question = question.lower()

    if any(
        word in question
        for word in [
            "stage",
            "version",
            "release"
        ]
    ):

        return context[
            "project"
        ][
            "current_stage"
        ]

    elif any(
        word in question
        for word in [
            "health",
            "healthy",
            "score"
        ]
    ):

        return context[
            "repository"
        ][
            "health_score"
        ]

    elif any(
        word in question
        for word in [
            "critical",
            "important"
        ]
    ):

        return context[
            "repository"
        ][
            "critical_symbols"
        ]

    elif any(
        word in question
        for word in [
            "risk",
            "risky"
        ]
    ):

        return context[
            "repository"
        ][
            "risky_symbols"
        ]

    elif any(
        word in question
        for word in [
            "direction",
            "heading",
            "future"
        ]
    ):

        return context[
            "repository"
        ][
            "project_direction"
        ]

    elif any(
        word in question
        for word in [
            "commit",
            "latest commit"
        ]
    ):

        return context[
            "project"
        ][
            "latest_commit"
        ]

    return "Unknown Question"