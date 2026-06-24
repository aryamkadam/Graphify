def translate_for_claude(pack):

    return {

        "target":
            "Claude",

        "project_story":

            (
                f"{pack['project']} "
                "is an AI Context Transfer Engine "
                "focused on preserving, restoring "
                "and transferring understanding."
            ),

        "goal":
            pack["goal"],

        "recommended_reading":

            [
                "bootstrap",
                "session_reconstruction"
            ]
    }


def translate_for_gemini(pack):

    return {

        "target":
            "Gemini",

        "summary":

            {
                "project":
                    pack["project"],

                "goal":
                    pack["goal"],

                "focus":
                    "AI Memory Infrastructure"
            }
    }


def translate_for_local(pack):

    return {

        "target":
            "Local LLM",

        "compact":

            (
                f"{pack['project']} | "
                f"{pack['goal']} | "
                "Focus=AI Memory Infrastructure"
            )
    }


def translate_context_pack_v2(
    pack,
    target_ai
):

    target_ai = target_ai.lower()

    if target_ai == "claude":

        return translate_for_claude(
            pack
        )

    elif target_ai == "gemini":

        return translate_for_gemini(
            pack
        )

    elif target_ai == "local":

        return translate_for_local(
            pack
        )

    return pack