"""
Stage 19.2

Universal Context Serializer

Converts the Universal Repository Context
into a portable file that any AI can later
reload.

This becomes the foundation for AI transfer.
"""

import json
from pathlib import Path


class UniversalContextSerializer:

    FILE_EXTENSION = ".graphify"

    def save(

        self,

        context,

        output_directory="exports",

        file_name="repository_context",

    ):

        Path(output_directory).mkdir(

            parents=True,

            exist_ok=True,

        )

        file_path = (

            Path(output_directory)

            / f"{file_name}{self.FILE_EXTENSION}"

        )

        with open(

            file_path,

            "w",

            encoding="utf-8",

        ) as file:

            json.dump(

                context,

                file,

                indent=4,

                ensure_ascii=False,

            )

        return {

            "status": "success",

            "file_path": str(file_path),

            "size_bytes": file_path.stat().st_size,

            "portable": True,

            "format": self.FILE_EXTENSION,

        }

    # --------------------------------------------

    def load(

        self,

        file_path,

    ):

        with open(

            file_path,

            "r",

            encoding="utf-8",

        ) as file:

            context = json.load(file)

        return context