def build_ultimate_memory_pack():

    files = [

        "graphify-out/repository_context.md",

        "graphify-out/repository_brain.json",

        "graphify-out/architecture_summary.md",

        "graphify-out/repository_timeline.md",

        "graphify-out/decision_memory.md",

        "graphify-out/ai_handover_pack.md"
    ]

    sections = []

    sections.append(
        "# Ultimate Memory Pack"
    )

    sections.append("")

    for file_path in files:

        try:

            with open(
                file_path,
                "r",
                encoding="utf-8"
            ) as file:

                sections.append(
                    file.read()
                )

                sections.append("")

                sections.append(
                    "=" * 60
                )

                sections.append("")

        except FileNotFoundError:

            sections.append(
                f"Missing file: {file_path}"
            )

            sections.append("")

    return "\n".join(
        sections
    )
