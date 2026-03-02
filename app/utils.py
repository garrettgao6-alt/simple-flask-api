from urllib.parse import urlparse


def validate_url(url: str):
    parsed = urlparse(url)

    if parsed.scheme not in ("http", "https"):
        raise ValueError("Only http and https allowed")

    hostname = parsed.hostname

    if hostname in ("localhost", "127.0.0.1"):
        raise ValueError("Access to localhost is forbidden")

    if hostname and hostname.startswith("169.254."):
        raise ValueError("Access to metadata service forbidden")

    return True
