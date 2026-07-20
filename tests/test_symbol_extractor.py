from pathlib import Path
from pprint import pprint

from graph_builder.symbols.symbol_extractor import (
    SymbolExtractor,
)

print("\n========================================")
print("Symbol Extractor")
print("========================================\n")

target = (
    Path(__file__).resolve().parent.parent
    / "graph_builder"
    / "parser"
    / "python_ast_parser.py"
)

symbols = SymbolExtractor().extract(target)

print("Summary\n")

print(f"Symbols Extracted : {len(symbols)}")

print("\nSymbols\n")

for symbol in symbols:

    pprint(symbol.to_dict())