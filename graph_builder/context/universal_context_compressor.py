"""
Stage 19.3

Universal Context Compressor

Compresses Graphify's Universal Repository
Context into a compact transferable format.
"""

import gzip
import json
from pathlib import Path


class UniversalContextCompressor:

    FILE_EXTENSION = ".gctx"

    def compress(

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

        raw = json.dumps(

            context,

            ensure_ascii=False,

            indent=None,

        ).encode("utf-8")

        with gzip.open(

            file_path,

            "wb",

        ) as file:

            file.write(raw)

        return {

            "status": "success",

            "compressed_file": str(file_path),

            "compressed_size": file_path.stat().st_size,

            "format": self.FILE_EXTENSION,

            "portable": True,

        }

    # ----------------------------------------

    def decompress(

        self,

        file_path,

    ):

        with gzip.open(

            file_path,

            "rb",

        ) as file:

            raw = file.read()

        return json.loads(

            raw.decode("utf-8")

        )