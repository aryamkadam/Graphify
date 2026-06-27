from pprint import pprint

from graph_builder.knowledge_graph.import_parser import (
    ImportParser
)

parser = ImportParser(".")

edges = parser.parse_imports()

print("\nImport Relationships\n")

pprint(edges[:30])

print("\nTotal Relationships:", len(edges))