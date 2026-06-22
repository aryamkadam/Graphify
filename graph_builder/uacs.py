def build_uacs(
    universal_context
):

    uacs = {

        "uacs_version":
            "1.0",

        "project":
            universal_context[
                "project"
            ],

        "repository":
            universal_context[
                "repository"
            ],

        "github":
            universal_context[
                "github"
            ],

        "decisions":
            universal_context[
                "decisions"
            ],

        "sessions":
            universal_context[
                "sessions"
            ]
    }

    return uacs