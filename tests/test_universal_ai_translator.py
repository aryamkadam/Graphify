from pprint import pprint

from graph_builder.context.universal_repository_context import (
    UniversalRepositoryContext,
)

from graph_builder.context.universal_ai_translator import (
    UniversalAITranslator,
)

executive_brain = {

    "identity": {

        "phase": "Stabilization",

        "technical_direction": "Positive",

        "brain_state": "Growing",

    },

    "strategy": {

        "engineering_strategy":
        "Repository-wide Refactoring"

    },

    "priorities": {

        "highest_priority": {

            "task":
            "Remove Technical Debt"

        }

    },

    "planner": {

        "summary":
        "3 engineering sprints generated."

    },

    "decision": {

        "next_engineering_action":
        "Remove Technical Debt"

    },

    "future_direction":
    "Remove Technical Debt",

    "summary":
    "Repository Executive Brain ready."

}

memory = {

    "memory_strength": 0.60

}

story = {

    "summary":
    "Repository has evolved positively."

}

consciousness = {

    "phase":
    "Stabilization"

}

context = UniversalRepositoryContext().build(

    executive_brain,

    memory,

    story,

    consciousness,

)

translator = UniversalAITranslator()

print("\n============================")
print("ChatGPT Context")
print("============================")

pprint(

    translator.translate(

        context,

        "chatgpt",

    )

)

print("\n============================")
print("Claude Context")
print("============================")

pprint(

    translator.translate(

        context,

        "claude",

    )

)

print("\n============================")
print("Gemini Context")
print("============================")

pprint(

    translator.translate(

        context,

        "gemini",

    )

)