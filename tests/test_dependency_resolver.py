from pprint import pprint

from graph_builder.knowledge_graph.import_parser import (
    ImportParser
)

from graph_builder.knowledge_graph.dependency_resolver import (
    DependencyResolver
)

parser = ImportParser(".")

edges = parser.parse_imports()

resolver = DependencyResolver(".")

resolved = resolver.resolve(edges)

print("\nResolved Dependencies\n")

pprint(resolved[:40])

print("\nResolved:", sum(e["resolved"] for e in resolved))
print("Unresolved:", sum(not e["resolved"] for e in resolved))