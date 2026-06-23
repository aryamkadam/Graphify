def ask_context_reason(
    context,
    question
):

    question = question.lower()

    repository = context["repository"]

    github = context["github"]

    if "health" in question:

        return {

            "question":
                question,

            "answer":
                (
                    f"Health score is "
                    f"{repository['health_score']} "
                    f"because repository contains "
                    f"{repository['dead_code_count']} dead symbols and "
                    f"{repository['hotspot_count']} hotspots."
                )
        }

    if "maturity" in question:

        return {

            "question":
                question,

            "answer":
                (
                    f"Repository maturity is "
                    f"{github['maturity']['maturity_level']} "
                    f"because project has "
                    f"{github['activity']['total_commits']} commits and "
                    f"{github['releases']['release_count']} releases."
                )
        }

    if "direction" in question:

        return {

            "question":
                question,

            "answer":
                (
                    f"Current project direction is "
                    f"{repository['project_direction']} "
                    f"based on decision analysis."
                )
        }

    if "risk" in question:

        return {

            "question":
                question,

            "answer":
                (
                    "Repository risks are concentrated around: "
                    + ", ".join(
                        repository["risky_symbols"]
                    )
                )
        }

    return {

        "question":
            question,

        "answer":
            "No reasoning rule found."
    }