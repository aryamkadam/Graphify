def detect_query_intent(
    query
):

    query = query.lower()

    if (
        "critical" in query
        or "important" in query
    ):
        return "critical_symbols"

    if (
        "dead code" in query
        or "unused" in query
    ):
        return "dead_code"

    if (
        "risk" in query
        or "risky" in query
    ):
        return "risky_symbols"

    if (
        "hotspot" in query
        or "hotspots" in query
    ):
        return "hotspots"

    if (
        "impact" in query
        or "change" in query
    ):
        return "impact"

    if (
        "find" in query
        or "search" in query
    ):
        return "search"

    return "unknown"