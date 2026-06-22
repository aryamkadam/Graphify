from pprint import pprint

from graph_builder.ai_transfer_memory import (
    save_transfer,
    get_transfer_history
)

save_transfer("ChatGPT")
save_transfer("Claude")
save_transfer("Gemini")

pprint(
    get_transfer_history()
)