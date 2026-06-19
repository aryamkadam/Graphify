def find_duplicates(files):

    hash_map = {}

    for file in files:

        sha = file.get("sha256")

        if not sha:
            continue

        hash_map.setdefault(
            sha,
            []
        ).append(file["path"])

    duplicates = []

    for sha, paths in hash_map.items():

        if len(paths) > 1:

            duplicates.append({
                "sha256": sha,
                "files": paths
            })

    return duplicates