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
            "identity"
        ][
            "current_stage"
        ]

    elif any(
        word in question
        for word in [
            "goal",
            "purpose",
            "mission"
        ]
    ):

        return context[
            "identity"
        ][
            "goal"
        ]

    elif any(
        word in question
        for word in [
            "project",
            "name"
        ]
    ):

        return context[
            "identity"
        ][
            "project_name"
        ]

    elif any(
        word in question
        for word in [
            "quality",
            "transfer",
            "score"
        ]
    ):

        return context[
            "quality"
        ][
            "transfer_score"
        ]

    elif any(
        word in question
        for word in [
            "decision",
            "decisions"
        ]
    ):

        return context[
            "decisions"
        ]

    elif any(
        word in question
        for word in [
            "history",
            "context history"
        ]
    ):

        return context[
            "history"
        ]

    elif any(
        word in question
        for word in [
            "next",
            "future",
            "continuation"
        ]
    ):

        return context[
            "continuation"
        ]

    elif any(
        word in question
        for word in [
            "reconstruction",
            "summary"
        ]
    ):

        return context[
            "reconstruction"
        ]

    return "Unknown Question"