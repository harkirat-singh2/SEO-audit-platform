"""
parser.py

create_soup()

Title
│
├── extract_title()
├── extract_meta_description()
├── extract_meta_keywords()

Headings
│
├── extract_headings()
├── extract_h1()

Links
│
├── extract_links()
├── extract_canonical()
├── extract_robots_meta()

Images
│
├── extract_images()
├── extract_images_without_alt()

Content
│
├── count_words()
├── extract_language()

Social
│
├── extract_open_graph()
├── extract_twitter_cards()

Structured Data
│
└── extract_schema_markup()
"""

from bs4 import BeautifulSoup


def create_soup(html: str) -> BeautifulSoup:
    """
    Convert HTML into a BeautifulSoup object for parsing.
    """
    return BeautifulSoup(html, "html.parser")


# ------------------------------------------------------------------
# Title
# ------------------------------------------------------------------

def extract_title(soup: BeautifulSoup) -> str | None:
    """
    Extract the page title.
    """
    if soup.title:
        return soup.title.get_text(strip=True)

    return None


def extract_meta_description(soup: BeautifulSoup) -> str | None:
    """
    Extract the meta description.
    """
    meta_description = soup.find(
        "meta",
        attrs={"name": "description"},
    )

    if meta_description:
        content = meta_description.get("content")
        return content.strip() if content else None

    return None


def extract_meta_keywords(soup: BeautifulSoup) -> str | None:
    """
    Extract the meta keywords.
    """
    meta_keywords = soup.find(
        "meta",
        attrs={"name": "keywords"},
    )

    if meta_keywords:
        content = meta_keywords.get("content")
        return content.strip() if content else None

    return None


# ------------------------------------------------------------------
# Headings
# ------------------------------------------------------------------

def extract_headings(
    soup: BeautifulSoup,
) -> dict[str, list[str]]:
    """
    Extract all headings (H1-H6).
    """
    headings: dict[str, list[str]] = {}

    for level in range(1, 7):
        tag = f"h{level}"

        headings[tag] = [
            heading.get_text(strip=True)
            for heading in soup.find_all(tag)
        ]

    return headings


def extract_h1(
    soup: BeautifulSoup,
) -> list[str]:
    """
    Extract all H1 headings.
    """
    return extract_headings(soup)["h1"]


# ------------------------------------------------------------------
# Links
# ------------------------------------------------------------------

def extract_links(
    soup: BeautifulSoup,
) -> list[str]:
    """
    Extract all hyperlinks.
    """
    links: list[str] = []

    for tag in soup.find_all("a"):
        href = tag.get("href")

        if href:
            links.append(href)

    return links


def extract_canonical(
    soup: BeautifulSoup,
) -> str | None:
    """
    Extract the canonical URL.
    """
    canonical = soup.find(
        "link",
        rel="canonical",
    )

    if canonical:
        return canonical.get("href")

    return None


def extract_robots_meta(
    soup: BeautifulSoup,
) -> dict[str, bool] | None:
    """
    Extract robots meta directives.
    """
    robots = soup.find(
        "meta",
        attrs={"name": "robots"},
    )

    if robots:
        content = robots.get("content")

        if content:
            directives = {
                item.strip().lower()
                for item in content.split(",")
            }

            return {
                "index": "noindex" not in directives,
                "follow": "nofollow" not in directives,
            }

    return None


# ------------------------------------------------------------------
# Images
# ------------------------------------------------------------------

def extract_images(
    soup: BeautifulSoup,
) -> list[str]:
    """
    Extract image URLs.
    """
    images: list[str] = []

    for tag in soup.find_all("img"):
        src = tag.get("src")

        if src:
            images.append(src)

    return images


def extract_images_without_alt(
    soup: BeautifulSoup,
) -> list[str]:
    """
    Extract image URLs missing alt text.
    """
    images: list[str] = []

    for tag in soup.find_all("img"):
        alt = tag.get("alt")

        if not alt:
            src = tag.get("src")

            if src:
                images.append(src)

    return images


# ------------------------------------------------------------------
# Content
# ------------------------------------------------------------------

def count_words(
    soup: BeautifulSoup,
) -> int:
    """
    Count visible words on the page.
    """
    text = soup.get_text(
        separator=" ",
        strip=True,
    )

    return len(text.split())


def extract_language(
    soup: BeautifulSoup,
) -> str | None:
    """
    Extract the page language.
    """
    html = soup.find("html")

    if html:
        lang = html.get("lang")

        return lang.strip() if lang else None

    return None


# ------------------------------------------------------------------
# Social
# ------------------------------------------------------------------

def extract_open_graph(
    soup: BeautifulSoup,
) -> dict[str, str] | None:
    """
    Extract Open Graph meta tags.
    """
    open_graph: dict[str, str] = {}

    for tag in soup.find_all(
        "meta",
        property=lambda value: value and value.startswith("og:"),
    ):
        property_name = tag.get("property")
        content = tag.get("content")

        if property_name and content:
            open_graph[property_name] = content

    return open_graph or None


def extract_twitter_cards(
    soup: BeautifulSoup,
) -> dict[str, str] | None:
    """
    Extract Twitter Card meta tags.
    """
    twitter_cards: dict[str, str] = {}

    for tag in soup.find_all(
        "meta",
        attrs={
            "name": lambda value: value and value.startswith("twitter:")
        },
    ):
        name = tag.get("name")
        content = tag.get("content")

        if name and content:
            twitter_cards[name] = content

    return twitter_cards or None


# ------------------------------------------------------------------
# Structured Data
# ------------------------------------------------------------------

def extract_schema_markup(
    soup: BeautifulSoup,
) -> list[str]:
    """
    Extract Schema.org JSON-LD blocks.
    """
    return [
        tag.get_text(strip=True)
        for tag in soup.find_all(
            "script",
            type="application/ld+json",
        )
    ]