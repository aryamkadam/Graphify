import hashlib
import json


def generate_context_signature(
    context_pack
):

    content = json.dumps(

        context_pack,

        sort_keys=True
    )

    signature = hashlib.sha256(

        content.encode(
            "utf-8"
        )

    ).hexdigest()

    return signature


def verify_context_signature(

    context_pack,

    signature
):

    expected = (

        generate_context_signature(
            context_pack
        )
    )

    return expected == signature