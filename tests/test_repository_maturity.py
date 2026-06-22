from pprint import pprint

from graph_builder.repository_maturity import (
    calculate_repository_maturity
)

print(
    "\nRepository Maturity Generated\n"
)

pprint(
    calculate_repository_maturity()
)