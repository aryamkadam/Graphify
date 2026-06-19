from pathlib import Path
from datetime import datetime

from rich.progress import track

from scanner.classifier import classify_file
from scanner.hash_utils import calculate_sha256


DEFAULT_IGNORES = {
    ".git",
    ".venv",
    "__pycache__",
    "graphify-out",
    "node_modules",
    "dist",
    "build",
    ".idea",
    ".vscode"
}


def scan_repository(root_path, ignore_spec=None):

    indexed_files = []
    file_counter = 1

    all_files = list(
        Path(root_path).rglob("*")
    )

    for file in track(
        all_files,
        description="Scanning..."
    ):

        if not file.is_file():
            continue

        if any(
            part in DEFAULT_IGNORES
            for part in file.parts
        ):
            continue

        relative_path = str(
            file.relative_to(root_path)
        )

        if (
            ignore_spec
            and ignore_spec.match_file(
                relative_path
            )
        ):
            continue

        file_info = {
            "id": f"file_{file_counter}",
            "path": relative_path,
            "type": classify_file(
                relative_path
            ),
            "size": file.stat().st_size,
            "modified": datetime.fromtimestamp(
                file.stat().st_mtime
            ).isoformat(),
            "sha256": calculate_sha256(
                file
            )
        }

        indexed_files.append(
            file_info
        )

        file_counter += 1

    return indexed_files