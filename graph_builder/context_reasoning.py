def ask_context_reason(
    context,
    question
):

    question = question.lower()

    identity = context.get(
        "identity",
        {}
    )

    quality = context.get(
        "quality",
        {}
    )

    continuation = context.get(
        "continuation",
        {}
    )

    decisions = context.get(
        "decisions",
        {}
    )

    if "health" in question:

        return {

            "question":
                question,

            "answer":
                (
                    f"Transfer quality score is "
                    f"{quality.get('transfer_score',0)}. "
                    f"History coverage is "
                    f"{quality.get('history_coverage',0)} "
                    f"and decision coverage is "
                    f"{quality.get('decision_coverage',0)}."
                )
        }

    if "stage" in question:

        return {

            "question":
                question,

            "answer":
                (
                    f"Current project stage is "
                    f"{identity.get('current_stage','unknown')}."
                )
        }

    if "goal" in question:

        return {

            "question":
                question,

            "answer":
                (
                    f"Project goal is "
                    f"{identity.get('goal','unknown')}."
                )
        }

    if "direction" in question:

        return {

            "question":
                question,

            "answer":
                (
                    f"Current direction is "
                    f"{continuation.get('next_objective','unknown')}."
                )
        }

    if "decision" in question:

        return {

            "question":
                question,

            "answer":
                (
                    f"Project contains "
                    f"{len(decisions.get('decision_history',[]))} "
                    f"tracked architectural decisions."
                )
        }

    return {

        "question":
            question,

        "answer":
            "No reasoning rule found."
    }