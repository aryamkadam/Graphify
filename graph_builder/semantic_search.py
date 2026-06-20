QUERY_EXPANSIONS = {

    "hashing": [
        "hash",
        "sha256",
        "checksum"
    ],

    "duplicate": [
        "duplicate",
        "duplicates"
    ],

    "parsing": [
        "parser",
        "parse"
    ],

    "scanner": [
        "scan",
        "scanner"
    ],

    "report": [
        "report",
        "generate"
    ]
}


def search_repository(
    query,
    symbol_index
):

    query_tokens = set()

    for token in query.lower().split():

        query_tokens.add(
            token
        )

        if token in QUERY_EXPANSIONS:

            query_tokens.update(
                QUERY_EXPANSIONS[token]
            )

    results = []

    for symbol, data in symbol_index.items():

        searchable_text = " ".join(
            [
                symbol,
                data["file"],
                data.get(
                    "docstring"
                ) or ""
            ]
        ).lower()

        score = 0

        for token in query_tokens:

            if token in searchable_text:

                score += 1

        if score > 0:

            results.append(
                {
                    "symbol": symbol,
                    "file": data["file"],
                    "type": data["type"],
                    "score": score
                }
            )

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return results