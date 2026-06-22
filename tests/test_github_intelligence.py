from pprint import pprint

from graph_builder.github_exporter import (
    export_github_intelligence
)

data = export_github_intelligence(
    "graphify-out/github_intelligence.json"
)

print(
    "\nGitHub Intelligence Generated\n"
)

pprint(data)