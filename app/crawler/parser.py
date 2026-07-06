from bs4 import BeautifulSoup
import logging

logger = logging.getLogger(__name__)


def create_soup(html:str) -> BeautifulSoup:
    """
    Convert HTML into a BeautifulSoup object for parsing.
    """
    return BeautifulSoup(html, "html.parser")

def extract_title(soup: BeautifulSoup) -> str | None:
    """
    Extract the page title.
    """
    if soup.title:
        return soup.title.get_text(strip=True)

    return None

def extract_meta_description(soup : BeautifulSoup) -> str | None:
    """
    Extract the meta description.
    """
    meta_description = soup.find("meta", attrs={"name": "description"})
    return meta_description["content"].strip() if meta_description else None


def extract_h1(soup : BeautifulSoup) -> list[str]:
    """
    Extract all H1 headings.
    """
    h1_tags = soup.find_all("h1") 

    return [h1.get_text(strip=True) for h1 in h1_tags]

def extract_links(soup : BeautifulSoup) -> list[str]:
    """
    Extract all the links from the page.
    """
    all_links = soup.find_all("a", href=True)
    return [link["href"] for link in all_links]

def extract_images(soup : BeautifulSoup) -> list[str]:
    """
    Extract all the images from the page.
    """
    all_images = soup.find_all("img", src=True)
    return [img["src"] for img in all_images]


def extract_canonical_url(soup : BeautifulSoup) -> str | None:
    """
    Extract the canonical URL.
    """
    canonical_url = soup.find("link", rel="canonical")
    return canonical_url["href"] if canonical_url else None

def extract_robots_meta(soup : BeautifulSoup) -> dict[str, bool] | None:
    """
    Extract the robots meta tag.
    """
    robots_meta = soup.find("meta", attrs={"name": "robots"})
    if robots_meta:
        content = robots_meta["content"].lower().split(",")
        return {"index": "noindex" not in content, "follow": "nofollow" not in content}
    return None    