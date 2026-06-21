import json


def create_decision(
    title,
    reason,
    impact,
    stage,
    commit=None
):

    decision = {

        "title":
            title,

        "reason":
            reason,

        "impact":
            impact,

        "stage":
            stage,

        "commit":
            commit
    }

    return decision