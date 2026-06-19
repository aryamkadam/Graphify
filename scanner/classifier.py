from pathlib import Path

FILE_TYPES = {
    ".py": "python",
    ".js": "javascript",
    ".ts": "typescript",
    ".sql": "sql",
    ".md": "markdown",
    ".json": "json",
    ".html": "html",
    ".css": "css"
}


def classify_file(filepath: str) -> str:
    ext = Path(filepath).suffix.lower()
    return FILE_TYPES.get(ext, "unknown")