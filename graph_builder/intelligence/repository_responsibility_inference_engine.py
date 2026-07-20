"""
Graphify

Phase 12

Stage P12.2

Repository Responsibility Inference Engine

Infers engineering responsibility from
repository structure instead of hardcoded mappings.

Author:
Graphify Core
"""


class RepositoryResponsibilityInferenceEngine:

    VERSION = "P12.2"

    def infer(

        self,

        module,

        symbols,

        relationships,

    ):

        words = []

        words.extend(

            self._tokenize(module["module_name"])

        )

        for symbol in symbols:

            words.extend(

                self._tokenize(symbol["name"])

            )

        for relation in relationships:

            words.extend(

                self._tokenize(relation["target"])

            )

        return {

            "module": module["module_name"],

            "responsibility": self._infer(words),

            "confidence": self._confidence(words),

            "keywords": sorted(set(words)),

            "version": self.VERSION,

        }

    # ---------------------------------------------

    def _tokenize(

        self,

        text,

    ):

        return [

            token.lower()

            for token in text.replace(".", "_").split("_")

            if token

        ]

    # ---------------------------------------------

    def _infer(

        self,

        words,

    ):

        if "learning" in words:

            return "Repository Learning"

        if "reasoning" in words:

            return "Engineering Reasoning"

        if "runtime" in words:

            return "Runtime Execution"

        if "planning" in words:

            return "Engineering Planning"

        if "memory" in words:

            return "Repository Memory"

        if "knowledge" in words:

            return "Repository Knowledge"

        if "graph" in words:

            return "Knowledge Graph"

        if "worker" in words:

            return "Engineering Worker"

        if "parser" in words:

            return "Repository Parsing"

        if "scanner" in words:

            return "Repository Scanning"

        return "General Repository Engineering"

    # ---------------------------------------------

    def _confidence(

        self,

        words,

    ):

        score = len(set(words))

        return round(

            min(1.0, 0.60 + score * 0.03),

            2,

        )