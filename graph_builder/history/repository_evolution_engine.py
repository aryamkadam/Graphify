"""
Stage 16.3

Repository Evolution Engine

Compares two repository snapshots and explains
how the repository has evolved.

This is the first step toward Repository History.

Future stages will detect:

- architectural drift
- engineering trends
- long-term evolution
- AI learning
"""

class RepositoryEvolutionEngine:

    def __init__(self, old_snapshot, new_snapshot):

        self.old = old_snapshot
        self.new = new_snapshot

    # --------------------------------------------

    def _health_change(self):

        old_score = self.old["health"]["health_score"]
        new_score = self.new["health"]["health_score"]

        delta = new_score - old_score

        if delta > 0:
            status = "improved"

        elif delta < 0:
            status = "declined"

        else:
            status = "unchanged"

        return {

            "old": old_score,

            "new": new_score,

            "delta": delta,

            "status": status

        }

    # --------------------------------------------

    def _execution_change(self):

        old_nodes = self.old["execution"]["graph_nodes"]
        new_nodes = self.new["execution"]["graph_nodes"]

        delta = new_nodes - old_nodes

        if delta > 0:
            status = "expanded"

        elif delta < 0:
            status = "reduced"

        else:
            status = "unchanged"

        return {

            "old": old_nodes,

            "new": new_nodes,

            "delta": delta,

            "status": status

        }

    # --------------------------------------------

    def _knowledge_change(self):

        old_dead = self.old["knowledge"]["dead_code_count"]
        new_dead = self.new["knowledge"]["dead_code_count"]

        old_hotspots = self.old["knowledge"]["hotspot_count"]
        new_hotspots = self.new["knowledge"]["hotspot_count"]

        return {

            "dead_code": {

                "old": old_dead,

                "new": new_dead,

                "delta": new_dead - old_dead

            },

            "hotspots": {

                "old": old_hotspots,

                "new": new_hotspots,

                "delta": new_hotspots - old_hotspots

            }

        }

    # --------------------------------------------

    def _summary(self, health, execution, knowledge):

        parts = []

        if health["status"] == "improved":
            parts.append("Repository health improved.")

        elif health["status"] == "declined":
            parts.append("Repository health declined.")

        if execution["status"] == "expanded":
            parts.append("Execution graph expanded.")

        elif execution["status"] == "reduced":
            parts.append("Execution graph became smaller.")

        if knowledge["dead_code"]["delta"] < 0:
            parts.append("Dead code decreased.")

        elif knowledge["dead_code"]["delta"] > 0:
            parts.append("Dead code increased.")

        if knowledge["hotspots"]["delta"] < 0:
            parts.append("Repository hotspots decreased.")

        elif knowledge["hotspots"]["delta"] > 0:
            parts.append("Repository hotspots increased.")

        if not parts:
            return "Repository remained stable."

        return " ".join(parts)

    # --------------------------------------------

    def build(self):

        health = self._health_change()

        execution = self._execution_change()

        knowledge = self._knowledge_change()

        return {

            "health": health,

            "execution": execution,

            "knowledge": knowledge,

            "summary": self._summary(

                health,

                execution,

                knowledge

            )

        }