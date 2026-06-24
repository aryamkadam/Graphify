def translate_context_pack(
    transfer_pack,
    target_ai
):

    if target_ai == "claude":

        return {

            "target":
                "Claude",

            "format":
                "Narrative",

            "content":
                transfer_pack
        }

    elif target_ai == "gemini":

        return {

            "target":
                "Gemini",

            "format":
                "Summary",

            "content":
                transfer_pack
        }

    elif target_ai == "openai":

        return {

            "target":
                "OpenAI",

            "format":
                "Structured",

            "content":
                transfer_pack
        }

    elif target_ai == "local":

        return {

            "target":
                "Local LLM",

            "format":
                "Compact",

            "content":
                transfer_pack
        }

    return transfer_pack