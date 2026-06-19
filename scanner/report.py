from datetime import datetime


def generate_report(
    root,
    files,
    language_stats,
    duplicates,
    output_file
):

    total_size = sum(
        f["size"]
        for f in files
    )

    largest_files = sorted(
        files,
        key=lambda x: x["size"],
        reverse=True
    )[:10]

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as report:

        report.write(
            "# Graphify Scan Report\n\n"
        )

        report.write(
            f"Project: {root.name}\n\n"
        )

        report.write(
            f"Generated: {datetime.now().isoformat()}\n\n"
        )

        report.write(
            f"Total Files: {len(files)}\n"
        )

        report.write(
            f"Total Size: {total_size:,} bytes\n\n"
        )

        report.write(
            "## Language Statistics\n\n"
        )

        for lang, count in sorted(
            language_stats.items()
        ):
            report.write(
                f"- {lang}: {count}\n"
            )

        report.write(
            "\n## Largest Files\n\n"
        )

        for file in largest_files:
            report.write(
                f"- {file['path']} ({file['size']} bytes)\n"
            )

        report.write(
            f"\n## Duplicate Groups: {len(duplicates)}\n"
        )