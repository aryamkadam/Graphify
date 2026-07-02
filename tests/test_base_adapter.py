from pprint import pprint

from graph_builder.context.adapters.base_adapter import (
    BaseAdapter,
)

context = {

    "repository_identity": {

        "phase": "Stabilization",

        "technical_direction": "Positive",

    },

    "repository_strategy": {

        "engineering_strategy":
        "Repository-wide Refactoring",

    }

}

adapter = BaseAdapter()

print("\n========================================")
print("Base Adapter")
print("========================================\n")

pprint(

    adapter.adapt(

        context

    )

)

print("\nMetadata\n")

pprint(

    adapter.adapter_metadata()

)