from sdk.python.graphify.client import GraphifyClient

client = GraphifyClient()

context = client.build_context(".")

print(type(context))