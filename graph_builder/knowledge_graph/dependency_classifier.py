"""
Dependency Classifier

Stage 14.5

Classifies every dependency into:

- internal
- stdlib
- third_party
- unknown
"""

import sys


class DependencyClassifier:

    def __init__(self):

        self.stdlib = set(sys.stdlib_module_names)

    def classify(self, resolved_edges):

        classified = []

        for edge in resolved_edges:

            target = edge["target"]

            category = "unknown"

            if edge["resolved"]:

                category = "internal"

            elif target in self.stdlib:

                category = "stdlib"

            elif "." in target:

                category = "third_party"

            else:

                category = "third_party"

            classified.append({

                **edge,

                "category": category

            })

        return classified