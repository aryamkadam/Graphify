def normalize_context(
    raw_context,
    source_ai
):

    source_ai = source_ai.lower()

    normalized = {

        "identity": {},
        "history": {},
        "decisions": {},
        "reconstruction": {},
        "continuation": {},
        "quality": {}
    }

    if source_ai == "chatgpt":

        normalized["identity"] = {

            "project_name":
                raw_context.get(
                    "project"
                ),

            "current_stage":
                raw_context.get(
                    "stage"
                ),

            "goal":
                raw_context.get(
                    "goal"
                )
        }

    elif source_ai == "claude":

        normalized["identity"] = {

            "project_name":
                raw_context.get(
                    "project_name"
                ),

            "current_stage":
                raw_context.get(
                    "current_stage"
                ),

            "goal":
                raw_context.get(
                    "goal"
                )
        }

    elif source_ai == "gemini":

        normalized["identity"] = {

            "project_name":
                raw_context.get(
                    "workspace"
                ),

            "current_stage":
                raw_context.get(
                    "status"
                ),

            "goal":
                raw_context.get(
                    "goal"
                )
        }

    elif source_ai == "graphify":

        normalized = {

            "identity":
                raw_context.get(
                    "identity",
                    {}
                ),

            "history":
                raw_context.get(
                    "history",
                    {}
                ),

            "decisions":
                raw_context.get(
                    "decisions",
                    {}
                ),

            "reconstruction":
                raw_context.get(
                    "reconstruction",
                    {}
                ),

            "continuation":
                raw_context.get(
                    "continuation",
                    {}
                ),

            "quality":
                raw_context.get(
                    "quality",
                    {}
                )
        }

    return normalized