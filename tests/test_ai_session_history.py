from pprint import pprint

from graph_builder.ai_session import (
    create_ai_session
)

from graph_builder.ai_session_history import (
    save_ai_session
)

session = create_ai_session(

    title=
    "GitHub Intelligence",

    topic=
    "Stage 6.5",

    summary=
    "Built GitHub health and maturity engine.",

    stage=
    "stage-6.5-stable"
)

history = save_ai_session(
    session
)

print(
    "\nAI Session History Updated\n"
)

pprint(
    history
)