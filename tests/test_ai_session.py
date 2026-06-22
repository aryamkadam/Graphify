from pprint import pprint

from graph_builder.ai_session import (
    create_ai_session
)

session = create_ai_session(

    title=
    "Decision Intelligence",

    topic=
    "Stage 6.3",

    summary=
    "Implemented decision engine and reasoning pack.",

    stage=
    "stage-6.3-stable"
)

print(
    "\nAI Session Generated\n"
)

pprint(
    session
)