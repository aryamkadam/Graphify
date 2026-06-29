"""
Stage 17.1

Repository Timeline Engine

Creates a chronological timeline of repository evolution
using Repository Evolution Reports.
"""


class RepositoryTimelineEngine:

    def build(self, evolution_history):

        if not evolution_history:

            return {

                "events": [],

                "timeline_summary": ""

            }

        events = []

        previous = None

        for index, report in enumerate(evolution_history):

            event = {

                "timestamp": report.get(
                    "timestamp",
                    f"Snapshot {index + 1}"
                ),

                "health": report["health"]["new"],

                "execution_nodes": report["execution"]["new"],

                "direction": "Positive"
                if report["health"]["delta"] >= 0
                else "Negative",

                "maturity": "Growing"

            }

            # ------------------------------------

            if previous is None:

                event["change"] = "Repository Baseline"

            else:

                if event["health"] > previous["health"]:

                    event["change"] = "Health Improved"

                elif event["health"] < previous["health"]:

                    event["change"] = "Health Declined"

                elif (

                    event["execution_nodes"]

                    >

                    previous["execution_nodes"]

                ):

                    event["change"] = "Execution Expanded"

                else:

                    event["change"] = "Repository Stable"

            events.append(event)

            previous = event

        return {

            "events": events,

            "timeline_summary": self._summary(events)

        }

    # ---------------------------------------------

    def _summary(self, events):

        if len(events) <= 1:

            return "Repository timeline has just started."

        improvements = sum(

            1

            for event in events

            if event["change"] == "Health Improved"

        )

        expansions = sum(

            1

            for event in events

            if event["change"] == "Execution Expanded"

        )

        return (

            f"{len(events)} repository snapshots recorded. "

            f"{improvements} health improvements detected. "

            f"{expansions} execution expansions observed."

        )