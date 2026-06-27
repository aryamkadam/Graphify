from collections import defaultdict


class ReverseCallIndex:

    def build(self, execution_graph):

        reverse = defaultdict(list)

        for caller, callees in execution_graph.items():

            for callee in callees:

                reverse[callee].append(caller)

        return dict(reverse)