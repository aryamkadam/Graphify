def generate_decision_categories(
    decisions
):

    categories = {

        "architecture": 0,
        "memory": 0,
        "metadata": 0,
        "context": 0,
        "other": 0
    }

    for decision in decisions:

        title = (
            decision["title"]
            .lower()
        )

        if (
            "brain" in title
            or
            "architecture" in title
        ):

            categories[
                "architecture"
            ] += 1

        elif (
            "memory" in title
        ):

            categories[
                "memory"
            ] += 1

        elif (
            "metadata" in title
        ):

            categories[
                "metadata"
            ] += 1

        elif (
            "context" in title
            or
            "handover" in title
        ):

            categories[
                "context"
            ] += 1

        else:

            categories[
                "other"
            ] += 1

    return categories