"""
Graphify

Phase 3

Stage P3.4

Engineering Planning Engine
"""
from graph_builder.executive.engineering_plan import (
    EngineeringPlan,
)

class EngineeringPlanningEngine:

	VERSION = "P3.4"

	def __init__(self, reasoning_engine):

		self.reasoning = reasoning_engine

	# --------------------------------------------------

	def generate_plan(self):

		decision = self.reasoning.reason()

		strategy = decision["strategy"]

		if strategy == "EXPANSION":

			tasks = [

				"Analyze repository coupling",

				"Improve repository architecture",

				"Implement new engineering capability",

			]

		elif strategy == "OPTIMIZATION":

			tasks = [

				"Reduce technical debt",

				"Optimize existing modules",

			]

		else:

			tasks = [

				"Stabilize repository",

				"Repair engineering foundation",

			]

		return EngineeringPlan(

    strategy=strategy,

    objective=decision["recommendation"],

    priority=decision["priority"],

    tasks=tasks,

    assigned_roles=[

        "architecture",

        "implementation",

        "testing",

    ],

)