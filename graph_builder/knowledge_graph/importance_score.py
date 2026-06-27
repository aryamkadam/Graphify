"""
Importance Score Engine

Ranks repository functions based on
their overall importance.

Stage 14.9.2
"""

from collections import Counter

IGNORED_FUNCTIONS = {
    "print",
    "pprint",
    "len",
    "sum",
    "min",
    "max",
    "sorted",
    "open",
    "set",
    "list",
    "dict",
    "tuple",
    "str",
    "int",
    "float",
    "bool",
    "round",
    "enumerate",
    "any",
    "all",
    "Path",
    "Counter",
    "isinstance"
}


class ImportanceScoreEngine:

    def __init__(self, execution_paths):

        self.execution_paths = execution_paths

    def calculate(self):

        frequency = Counter()

        downstream = Counter()

        entry_bonus = Counter()

        for path in self.execution_paths:

            functions = path["path"]

            if len(functions) == 0:
                continue

            # First function gets entry bonus
            if functions[0] not in IGNORED_FUNCTIONS:
             entry_bonus[functions[0]] = 50

            for function in functions:

             if function in IGNORED_FUNCTIONS:
              continue

             frequency[function] += 1

            # Downstream importance
            for i, function in enumerate(functions):

             if function in IGNORED_FUNCTIONS:
              continue

            downstream[function] += len(functions) - i - 11

        results = []

        all_functions = set(frequency.keys())

        for function in all_functions:

            score = (

                frequency[function]

                + downstream[function]

                + entry_bonus[function]

            )

            results.append({

                "function": function,

                "frequency": frequency[function],

                "downstream": downstream[function],

                "entry_bonus": entry_bonus[function],

                "score": score

            })

        results.sort(

            key=lambda x: x["score"],

            reverse=True

        )

        return results