from pathlib import Path
from pprint import pprint

from graph_builder.relationships.relationship_extractor import (
    RelationshipExtractor,
)

print("\n========================================")
print("Relationship Extractor")
print("========================================\n")

target = (
    Path(__file__).resolve().parent.parent
    / "graph_builder"
    / "parser"
    / "python_ast_parser.py"
)

relationships = RelationshipExtractor().extract(target)

print("Relationships Extracted :", len(relationships))

print()

for relation in relationships:

    pprint(relation.to_dict())