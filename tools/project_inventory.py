"""
Graphify

Architecture Audit

Project Inventory Generator

Generates a complete inventory of the repository.

Author:
Graphify Core
"""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


EXCLUDED = {
    ".git",
    ".venv",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".idea",
    ".vscode",
}


def main():

    print("\n========================================")
    print("GRAPHIFY PROJECT INVENTORY")
    print("========================================\n")

    for path in sorted(ROOT.rglob("*")):

        relative = path.relative_to(ROOT)

        if any(part in EXCLUDED for part in relative.parts):
            continue

        print(relative)


if __name__ == "__main__":
    main()