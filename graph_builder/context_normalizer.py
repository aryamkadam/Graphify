def normalize_context(
    raw_context,
    source_ai
):

    normalized = {

        "project_name":
            None,

        "current_stage":
            None
    }

    if source_ai == "ChatGPT":

        normalized[
            "project_name"
        ] = raw_context.get(
            "project"
        )

        normalized[
            "current_stage"
        ] = raw_context.get(
            "stage"
        )

    elif source_ai == "Claude":

        normalized[
            "project_name"
        ] = raw_context.get(
            "project_name"
        )

        normalized[
            "current_stage"
        ] = raw_context.get(
            "current_stage"
        )

    elif source_ai == "Gemini":

        normalized[
            "project_name"
        ] = raw_context.get(
            "workspace"
        )

        normalized[
            "current_stage"
        ] = raw_context.get(
            "status"
        )

    return normalized