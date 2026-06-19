import json
import time
from pathlib import Path
from datetime import datetime

import typer
from rich.console import Console

from scanner.scanner import scan_repository
from scanner.ignore import load_ignore_patterns
from scanner.duplicates import find_duplicates

app = typer.Typer()
console = Console()


@app.command()
def scan(path: str = "."):

    root = Path(path)
    start_time = time.time()

    console.print("[cyan]GRAPHIFY v0.2[/cyan]")

    ignore_spec = load_ignore_patterns(root)

    files = scan_repository(
        root,
        ignore_spec
    )

    output_dir = root / "graphify-out"
    output_dir.mkdir(exist_ok=True)

    # File Index
    with open(
        output_dir / "file_index.json",
        "w",
        encoding="utf-8"
    ) as f:
        json.dump(files, f, indent=4)

    # Language Statistics
    language_stats = {}

    for file in files:
        file_type = file["type"]

        language_stats[file_type] = (
            language_stats.get(file_type, 0) + 1
        )

    # Duplicate Detection
    duplicates = find_duplicates(files)

    with open(
        output_dir / "duplicates.json",
        "w",
        encoding="utf-8"
    ) as f:
        json.dump(duplicates, f, indent=4)

    # Metrics
    total_size = sum(
        file["size"]
        for file in files
    )

    scan_duration = round(
        time.time() - start_time,
        2
    )

    largest_files = sorted(
        files,
        key=lambda x: x["size"],
        reverse=True
    )[:5]

    # Manifest
    manifest = {
        "project_name": root.name,
        "generated_at": datetime.now().isoformat(),
        "total_files": len(files),
        "total_size_bytes": total_size,
        "scan_duration_seconds": scan_duration,
        "duplicate_groups": len(duplicates),
        "languages": language_stats
    }

    with open(
        output_dir / "manifest.json",
        "w",
        encoding="utf-8"
    ) as f:
        json.dump(manifest, f, indent=4)

    # Cache
    cache = {}

    for file in files:
        cache[file["path"]] = {
            "sha256": file["sha256"],
            "modified": file["modified"]
        }

    with open(
        output_dir / "cache.json",
        "w",
        encoding="utf-8"
    ) as f:
        json.dump(cache, f, indent=4)

    # Report
    with open(
        output_dir / "SCAN_REPORT.md",
        "w",
        encoding="utf-8"
    ) as report:

        report.write("# Graphify Scan Report\n\n")
        report.write(f"Project: {root.name}\n\n")
        report.write(
            f"Generated: {datetime.now().isoformat()}\n\n"
        )
        report.write(
            f"Total Files: {len(files)}\n"
        )
        report.write(
            f"Total Size: {total_size:,} bytes\n\n"
        )

        report.write("## Language Statistics\n\n")

        for lang, count in sorted(
            language_stats.items()
        ):
            report.write(
                f"- {lang}: {count}\n"
            )

        report.write("\n## Largest Files\n\n")

        for file in largest_files:
            report.write(
                f"- {file['path']} ({file['size']} bytes)\n"
            )

        report.write(
            f"\n## Duplicate Groups: {len(duplicates)}\n"
        )

    console.print(
        f"[green]✓ Indexed {len(files)} files[/green]"
    )

    console.print(
        f"[green]✓ Found {len(duplicates)} duplicate groups[/green]"
    )

    console.print(
        "[green]✓ Generated manifest.json[/green]"
    )

    console.print(
        "[green]✓ Generated duplicates.json[/green]"
    )

    console.print(
        "[green]✓ Generated cache.json[/green]"
    )

    console.print(
        "[green]✓ Generated SCAN_REPORT.md[/green]"
    )


if __name__ == "__main__":
    app()