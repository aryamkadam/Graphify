from graph_builder.protocols.uacp.validator import (
    validate_uacp
)
from graph_builder.protocols.uacp.adapters.registry import (
    get_adapter
)

from graph_builder.protocols.uacp.validator import (
    validate_uacp
)


def translate_context(

    source_ai,

    target_ai,

    universal_context_schema

):

    source = get_adapter(source_ai)

    target = get_adapter(target_ai)

    if source is None:
        raise ValueError(
            f"Unknown source adapter: {source_ai}"
        )

    if target is None:
        raise ValueError(
            f"Unknown target adapter: {target_ai}"
        )

    #
    # Generate UACP
    #

    uacp = source(
        universal_context_schema
    )

    #
    # Verify protocol
    #

    validation = validate_uacp(
        uacp
    )

    if not validation["valid"]:

        raise ValueError(
            f"Invalid UACP: {validation}"
        )

    #
    # Translate
    #

    translated = dict(uacp)

    translated["metadata"] = dict(
        uacp["metadata"]
    )

    translated["metadata"]["translated_to"] = (
        target_ai
    )

    translated["metadata"]["translator"] = (
        "Graphify"
    )

    translated["metadata"]["verification"] = (
        "passed"
    )

    return translated