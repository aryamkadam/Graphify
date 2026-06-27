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
    "isinstance",
    "enumerate",
    "any",
    "all",
    "round",
    "Path",
    "Counter"

}

class CriticalExecutionPath:

    """
    Finds the most important execution
    paths inside the repository.
    """

    def __init__(self, execution_paths):

        self.execution_paths = execution_paths

    def analyze(self):

        counter = Counter()

        for path in self.execution_paths:

            for function in path["path"]:

              if function in IGNORED_FUNCTIONS:
               continue

              counter[function] += 1
            critical = []

        for function, count in counter.most_common(20):

            critical.append({

                "function": function,

                "frequency": count

            })

        return critical