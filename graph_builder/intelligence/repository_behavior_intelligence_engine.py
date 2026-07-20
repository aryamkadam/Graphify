"""
Graphify

Phase 12

Stage P12.3.1

Repository Behavior Intelligence Engine

Infers engineering behavior from
parsed repository symbols.

Consumes:
    PythonModule
    RepositorySymbol

Produces:
    Repository Behavior Intelligence

Author:
Graphify Core
"""

from graph_builder.parser.python_module import PythonModule
from graph_builder.symbols.repository_symbol import RepositorySymbol


class RepositoryBehaviorIntelligenceEngine:

    VERSION = "P12.3.1"

    # ------------------------------------------------

    def analyze(

        self,

        module: PythonModule,

        symbols: list[RepositorySymbol],

    ):

        function_names = [

            symbol.name.lower()

            for symbol in symbols

            if symbol.symbol_type == "FUNCTION"

        ]

        behaviors = []

        for function in function_names:

            behavior = self._infer_behavior(function)

            if behavior and behavior not in behaviors:

                behaviors.append(behavior)

        primary = (

            behaviors[0]

            if behaviors

            else "General Repository Engineering"

        )

        secondary = behaviors[1:]

        confidence = self._confidence(function_names)

        return {

            "module": module.module_name,

            "primary_behavior": primary,

            "secondary_behaviors": secondary,

            "behavior_keywords": function_names,

            "behavior_confidence": confidence,

            "version": self.VERSION,

        }

    # ------------------------------------------------

    def _infer_behavior(

        self,

        function: str,

    ):

        mapping = {

            "learn": "Repository Learning",

            "experience": "Repository Learning",

            "feedback": "Feedback Processing",

            "record": "Knowledge Recording",

            "knowledge": "Knowledge Management",

            "reason": "Engineering Reasoning",

            "plan": "Engineering Planning",

            "execute": "Runtime Execution",

            "dispatch": "Runtime Dispatching",

            "schedule": "Task Scheduling",

            "memory": "Repository Memory",

            "store": "Repository Memory",

            "graph": "Knowledge Graph",

            "scan": "Repository Scanning",

            "parse": "Repository Parsing",

            "validate": "Repository Validation",

            "analyze": "Repository Analysis",

            "build": "Repository Construction",

            "export": "Repository Export",

            "import": "Repository Import",

        }

        for keyword, behavior in mapping.items():

            if keyword in function:

                return behavior

        return None

    # ------------------------------------------------

    def _confidence(

        self,

        functions: list[str],

    ):

        if not functions:

            return 0.0

        unique = len(set(functions))

        return round(

            min(

                1.0,

                0.65 + unique * 0.05,

            ),

            2,

        )