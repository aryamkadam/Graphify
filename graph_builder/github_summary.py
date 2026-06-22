from graph_builder.github_intelligence import (
    generate_github_intelligence
)


def generate_github_summary():

    data = (
        generate_github_intelligence()
    )

    lines = []

    lines.append(
        "# GitHub Intelligence Summary"
    )

    lines.append("")

    lines.append(
        f"Repository Health: "
        f"{data['github_health']['github_health']}"
    )

    lines.append(
        f"Health Score: "
        f"{data['github_health']['score']}"
    )

    lines.append("")

    lines.append(
        f"Repository Maturity: "
        f"{data['maturity']['maturity_level']}"
    )

    lines.append(
        f"Maturity Score: "
        f"{data['maturity']['maturity_score']}"
    )

    lines.append("")

    lines.append(
        f"Top Contributor: "
        f"{data['contributor_ranking']['top_contributor']}"
    )

    lines.append(
        f"Growth Status: "
        f"{data['growth']['growth_status']}"
    )

    lines.append(
        f"Velocity Score: "
        f"{data['velocity']['velocity_score']}"
    )

    return "\n".join(
        lines
    )