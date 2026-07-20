from pprint import pprint

from graph_builder.runtime.runtime_engine import RuntimeEngine


def main():

    engine = RuntimeEngine()

    snapshot = {

        "changed": True,

        "reason": "Repository structure changed.",

    }

    result = engine.execute(

        snapshot,

    )

    print("\n========================================")
    print("Runtime Engine")
    print("========================================\n")

    pprint(result)


if __name__ == "__main__":
    main()