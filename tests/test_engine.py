from pprint import pprint

from graph_builder.engine import GraphifyEngine

engine = GraphifyEngine()

print("\nGraphify Context\n")

pprint(engine.context())