from pprint import pprint

from graph_builder.runtime.runtime_engine import RuntimeEngine


def main():

    print("\n========================================")
    print("PHASE 8 RUNTIME INTEGRATION")
    print("========================================\n")

    runtime = RuntimeEngine()

    snapshot = {

        "changed": True,

        "reason": "Repository structure changed.",

    }

    result = runtime.execute(

        snapshot,

    )

    checks = {

        "Repository Observer":
            result["event"]["event_type"] == "REPOSITORY_MODIFIED",

        "Repository Event":
            result["event"]["requires_engineering"],

        "Runtime Scheduler":
            result["runtime_status"] == "ENGINEERING_STARTED",

        "Engineering Cycle":
            result["cycle"]["status"] == "RUNNING",

        "Runtime Engine":
            result["version"] == "P8.6",

    }

    pprint(checks)

    print("\n----------------------------------------")

    overall = all(checks.values())

    print(

        "Overall Status :",

        "PASS" if overall else "FAIL",

    )

    print("----------------------------------------")

    print("\nPipeline Summary")

    pprint(result)


if __name__ == "__main__":
    main()