"""
File Analyzer

Analyzes individual files inside repository.
"""

import os


class FileAnalyzer:

    def analyze_file(self, file_path):

        try:

            with open(file_path, "r", encoding="utf-8") as f:

                content = f.read()

        except Exception:

            content = ""

        return {

            "file_path":
                file_path,

            "size":
                os.path.getsize(file_path),

            "lines":
                len(content.splitlines()),

            "is_empty":
                len(content.strip()) == 0,

            "extension":
                os.path.splitext(file_path)[1]
        }