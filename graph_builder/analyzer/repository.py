"""
Repository Analyzer (Stage 14)

Converts ANY repository into structured intelligence.
"""

import os

from .file_analyzer import FileAnalyzer


class RepositoryAnalyzer:

    def __init__(self, repository_path):

        self.repository_path = repository_path

        self.file_analyzer = FileAnalyzer()


    def analyze_structure(self):

        structure = []

        for root, dirs, files in os.walk(
            self.repository_path
        ):

            structure.append({

                "root": root,

                "directories": dirs,

                "files": files
            })

        return structure


    def analyze_files(self):

        file_data = []

        for root, _, files in os.walk(
            self.repository_path
        ):

            for file in files:

                file_path = os.path.join(
                    root,
                    file
                )

                file_data.append(

                    self.file_analyzer.analyze_file(
                        file_path
                    )
                )

        return file_data


    def analyze(self):

        return {

            "repository_path":
                self.repository_path,

            "structure":
                self.analyze_structure(),

            "files":
                self.analyze_files(),

            "status":
                "analyzed",

            "stage":
                "stage-14-stable"
        }