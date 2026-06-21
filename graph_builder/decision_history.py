from graph_builder.decision_engine import (
    create_decision
)


def build_decision_history():

    decisions = []

    decisions.append(

        create_decision(

            title=
            "Graphify Became AI Context Transfer Engine",

            reason=
            "Developers lose context when switching AI systems",

            impact=
            "Entire roadmap shifted toward AI handover",

            stage=
            "stage-5-stable"
        )
    )

    decisions.append(

        create_decision(

            title=
            "Repository Brain Introduced",

            reason=
            "Need single source of truth for AI context transfer",

            impact=
            "repository_brain.json generated",

            stage=
            "stage-6.1-stable",

            commit=
            "fc4e2b3"
        )
    )

    decisions.append(

        create_decision(

            title=
            "Project Memory Engine Introduced",

            reason=
            "Project should remember its own evolution",

            impact=
            "project_memory.json generated",

            stage=
            "stage-6.2-stable"
        )
    )

    decisions.append(

        create_decision(

            title=
            "Metadata Engine Introduced",

            reason=
            "Graphify should understand Git history",

            impact=
            "Repository metadata generated automatically",

            stage=
            "stage-6.2-stable"
        )
    )

    return decisions