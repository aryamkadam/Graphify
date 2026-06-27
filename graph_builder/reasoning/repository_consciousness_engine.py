"""
Stage 15.6

Repository Consciousness Engine

Builds the high-level identity of the repository.

This is NOT AI consciousness.

It represents:

- Identity
- Mission
- Direction
- Strengths
- Weaknesses
- Long-term evolution

Future reasoning engines,
LLMs and autonomous agents
consume this object.
"""


class RepositoryConsciousnessEngine:

    def __init__(self, intelligence):

        self.intelligence = intelligence

    # ------------------------------------------------

    def _identity(self):

        metadata = self.intelligence["identity"]

        return {

            "repository": metadata.get(

                "repository_name",

                "Unknown"

            ),

            "branch": metadata.get(

                "current_branch",

                "unknown"

            ),

            "latest_commit":

                metadata.get(

                    "latest_commit",

                    "unknown"

                )

        }

    # ------------------------------------------------

    def _mission(self):

        insights = self.intelligence["decisions"]["insights"]

        return (

            f"Repository is primarily focused on "

            f"{insights['dominant_area']}."

        )

    # ------------------------------------------------

    def _strengths(self):

        health = self.intelligence["health"]

        strengths = []

        if health["health_score"] >= 90:

            strengths.append(

                "Healthy architecture"

            )

        if len(

            self.intelligence["knowledge"]["critical_symbols"]

        ) > 0:

            strengths.append(

                "Clear critical modules"

            )

        if len(

            self.intelligence["execution"]["importance_ranking"]

        ) > 0:

            strengths.append(

                "Execution flow understood"

            )

        return strengths

    # ------------------------------------------------

    def _weaknesses(self):

        weaknesses = []

        knowledge = self.intelligence["knowledge"]

        if knowledge["dead_code"]:

            weaknesses.append(

                "Dead code exists"

            )

        if knowledge["risky_symbols"]:

            weaknesses.append(

                "High-risk symbols detected"

            )

        return weaknesses

    # ------------------------------------------------

    def _goal(self):

        health = self.intelligence["health"]["health_score"]

        if health >= 90:

            return (

                "Scale into an enterprise-grade repository."

            )

        elif health >= 70:

            return (

                "Continue improving architecture."

            )

        return (

            "Stabilize the repository before expansion."

        )

    # ------------------------------------------------

    def _evolution(self):

        commits = self.intelligence["identity"]["total_commits"]

        if commits < 20:

            return "Emerging"

        elif commits < 100:

            return "Growing"

        elif commits < 300:

            return "Maturing"

        return "Enterprise"

    # ------------------------------------------------

    def build(self):

        consciousness = {

            "identity":

                self._identity(),

            "mission":

                self._mission(),

            "strengths":

                self._strengths(),

            "weaknesses":

                self._weaknesses(),

            "goal":

                self._goal(),

            "evolution_stage":

                self._evolution()

        }

        return consciousness