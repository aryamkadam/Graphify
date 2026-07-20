"""
Graphify

Phase 5

Stage P5.15

Executive Directive Validator

Validates executive directives before
they are accepted into planning.

Author:
Graphify Core
"""


class ExecutiveDirectiveValidator:

    VERSION = "P5.15"

    # --------------------------------------------

    def build(

        self,

        registry,

    ):

        directives = registry.get(

            "executive_directives",

            [],

        )

        seen = set()

        duplicates = []

        valid = []

        invalid = []

        for directive in directives:

            strategy = directive.get(

                "strategy",

            )

            directive_id = directive.get(

                "directive_id",

            )

            tasks = directive.get(

                "directive",

                [],

            )

            if (

                not directive_id

                or not strategy

                or not tasks

            ):

                invalid.append(

                    directive

                )

                continue

            if strategy in seen:

                duplicates.append(

                    strategy

                )

                continue

            seen.add(

                strategy

            )

            valid.append(

                directive

            )

        return {

            "valid_directives": valid,

            "invalid_directives": invalid,

            "duplicates": duplicates,

            "validation_passed":

                len(invalid) == 0,

            "summary":

                (

                    f"{len(valid)} valid directives, "

                    f"{len(duplicates)} duplicate strategies, "

                    f"{len(invalid)} invalid directives."

                ),

            "version":

                self.VERSION,

        }