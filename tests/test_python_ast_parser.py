from pprint import pprint

from graph_builder.parser.python_ast_parser import (
    PythonASTParser,
)

print("\n========================================")
print("Python AST Parser")
print("========================================\n")

parser = PythonASTParser()

from pathlib import Path

target = Path(__file__).parent.parent / "graph_builder" / "parser" / "python_ast_parser.py"

module = parser.parse(target)

print("Summary\n")

pprint(

    module.summary()

)

print("\nModule\n")

pprint(

    module.to_dict()

)