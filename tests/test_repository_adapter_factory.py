"""
Stage 19.4.5

Test Repository Adapter Factory
"""

from pprint import pprint

from graph_builder.context.adapters.repository_adapter_factory import (
    RepositoryAdapterFactory,
)

factory = RepositoryAdapterFactory()

print("\n========================================")
print("Repository Adapter Factory")
print("========================================\n")

print("Supported Adapters\n")

pprint(factory.supported_adapters())

print("\nChatGPT Adapter\n")

chatgpt = factory.get("chatgpt")

print(type(chatgpt).__name__)

print("\nClaude Adapter\n")

claude = factory.get("claude")

print(type(claude).__name__)

print("\nGemini Adapter\n")

gemini = factory.get("gemini")

print(type(gemini).__name__)

print("\n========================================")
print("Unsupported Adapter Test")
print("========================================\n")

try:

    factory.get("deepseek")

except ValueError as e:

    print("Caught expected exception:")

    print(e)