import hashlib


def calculate_sha256(filepath):
    sha = hashlib.sha256()

    try:
        with open(filepath, "rb") as f:
            while chunk := f.read(8192):
                sha.update(chunk)

        return sha.hexdigest()

    except Exception:
        return None