from graph_builder.graphify_context_pack import (
    generate_graphify_context_pack
)

from graph_builder.graphify_pack_exporter import (
    export_graphify_pack
)

from graph_builder.graphify_pack_importer import (
    import_graphify_pack
)

from graph_builder.context_pack_verifier import (
    verify_context_pack
)


def execute_context_transfer():

    pack = (
        generate_graphify_context_pack()
    )

    file_path = (
        export_graphify_pack(
            pack
        )
    )

    imported_pack = (
        import_graphify_pack(
            file_path
        )
    )

    verification = (
        verify_context_pack(
            imported_pack
        )
    )

    return {

        "exported_file":
            file_path,

        "verified":
            verification[
                "verified"
            ],

        "status":

            (
                "TRANSFER_COMPLETE"

                if verification[
                    "verified"
                ]

                else

                "TRANSFER_FAILED"
            )
    }