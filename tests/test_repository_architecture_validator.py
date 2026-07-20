from pprint import pprint

from graph_builder.architecture.repository_architecture_index import (
    RepositoryArchitectureIndex,
)

from graph_builder.architecture.repository_architecture_validator import (
    RepositoryArchitectureValidator,
)

print()
print("=" * 40)
print("Repository Architecture Validator")
print("=" * 40)

index = RepositoryArchitectureIndex().build(".")

validator = RepositoryArchitectureValidator()

report = validator.validate(index)

print()
print("Architecture Report")
print()

pprint(report)