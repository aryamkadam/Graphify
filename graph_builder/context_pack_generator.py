from graph_builder.graphify_context_pack import (
    generate_graphify_context_pack
)


def generate_context_pack():

    pack = (
        generate_graphify_context_pack()
    )

    schema = pack[
        "schema"
    ]

    identity = schema[
        "identity"
    ]

    quality = schema[
        "quality"
    ]

    continuation = schema[
        "continuation"
    ]

    reconstruction = schema[
        "reconstruction"
    ]

    lines = []

    lines.append(
        "# Graphify Context Pack"
    )

    lines.append("")

    lines.append(
        "## Identity"
    )

    lines.append("")

    lines.append(
        f"Project Name: "
        f"{identity['project_name']}"
    )

    lines.append(
        f"Goal: "
        f"{identity['goal']}"
    )

    lines.append(
        f"Current Stage: "
        f"{identity['current_stage']}"
    )

    lines.append("")

    lines.append(
        "## Transfer Quality"
    )

    lines.append("")

    lines.append(
        f"Transfer Score: "
        f"{quality['transfer_score']}"
    )

    lines.append(
        f"Recommendation: "
        f"{quality['recommendation']}"
    )

    lines.append("")

    lines.append(
        "## Reconstruction Summary"
    )

    lines.append("")

    lines.append(
        reconstruction[
            "reconstruction_summary"
        ]
    )

    lines.append("")

    lines.append(
        "## Continuation Plan"
    )

    lines.append("")

    lines.append(
        f"Current State: "
        f"{continuation['current_state']}"
    )

    lines.append(
        f"Next Objective: "
        f"{continuation['next_objective']}"
    )

    lines.append("")

    lines.append(
        "Recommended Actions:"
    )

    for action in continuation[
        "recommended_actions"
    ]:

        lines.append(
            f"- {action}"
        )

    lines.append("")

    lines.append(
        "## AI Instructions"
    )

    lines.append(
        "Use Universal Context Schema as source of truth."
    )

    lines.append(
        "Use Context History for continuity."
    )

    lines.append(
        "Use Decision History for reasoning."
    )

    lines.append(
        "Resume development from current stage."
    )

    return "\n".join(
        lines
    )