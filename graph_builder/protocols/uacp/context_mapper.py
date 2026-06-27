"""
Graphify UACP Context Mapper

Converts Graphify Universal Context
into the UACP Context Schema.
"""


def map_identity(universal_context):

    project = universal_context.get(
        "project",
        {}
    )

    return {

        "project_name":
            project.get(
                "project_name",
                "Unknown"
            ),

        "goal":
            project.get(
                "goal",
                "Unknown"
            ),

        "current_stage":
            project.get(
                "current_stage",
                "Unknown"
            )
    }


def map_history(universal_context):

    repository = universal_context.get(
        "repository",
        {}
    )

    return {

        "current_stage":
            repository.get(
                "current_stage",
                "Unknown"
            ),

        "latest_commit":
            repository.get(
                "latest_commit",
                "Unknown"
            ),

        "total_commits":
            repository.get(
                "total_commits",
                0
            ),

        "latest_tag":
            repository.get(
                "latest_tag",
                "Unknown"
            ),

        "current_branch":
            repository.get(
                "current_branch",
                "Unknown"
            )
    }


def map_decisions(universal_context):

    decisions = universal_context.get(
        "decisions",
        {}
    )

    return {

        "decision_count":
            decisions.get(
                "decision_count",
                0
            ),

        "latest_decisions":
            decisions.get(
                "latest_decisions",
                []
            ),

        "most_important_decisions":
            decisions.get(
                "most_important_decisions",
                []
            )
    }


def map_reconstruction(universal_context):

    return {}


def map_continuation(universal_context):

    return {}


def map_quality(universal_context):

    return {}


def map_universal_context(universal_context):

    return {

        "identity":
            map_identity(
                universal_context
            ),

        "history":
            map_history(
                universal_context
            ),

        "decisions":
            map_decisions(
                universal_context
            ),

        "reconstruction":
            map_reconstruction(
                universal_context
            ),

        "continuation":
            map_continuation(
                universal_context
            ),

        "quality":
            map_quality(
                universal_context
            ),

        "schema_version":
            universal_context.get(
                "schema_version",
                "1.0"
            )
    }