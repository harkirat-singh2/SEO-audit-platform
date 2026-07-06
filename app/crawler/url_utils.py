from urllib.parse import urljoin, urlparse, urldefrag

def remove_fragment(url: str) -> str:
    """
    Remove the fragment (#...) from a URL.
    """
    clean_url, _ = urldefrag(url)
    return clean_url

def normalize_url(base_url: str, link: str) -> str:
    """
    Convert a relative URL into an absolute URL
    and remove fragments.
    """
    absolute_url = urljoin(base_url, link)
    return remove_fragment(absolute_url)

def is_valid_url(url: str) -> bool:
    """
    Check whether the URL uses HTTP or HTTPS.
    """
    parsed = urlparse(url)

    return parsed.scheme in ("http", "https")

def is_same_domain(base_url: str, candidate_url: str) -> bool:
    """
    Check whether two URLs belong to the same domain.
    """
    base_domain = urlparse(base_url).netloc
    candidate_domain = urlparse(candidate_url).netloc

    return base_domain == candidate_domain