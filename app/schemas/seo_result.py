from dataclasses import dataclass
from dataclasses import field

@dataclass
class SEOResult:
    """
    Represents the SEO analysis of a webpage.
    """

    # Basic page information
    url: str

    # Title
    title: str | None
    title_length: int

    # Meta Description
    meta_description: str | None
    meta_description_length: int

    # Content
    word_count: int

    # Headings
    h1_count: int
    h2_count: int
    total_headings: int

    # Images
    total_images: int
    images_without_alt: int

    # Links
    internal_links: int
    external_links: int

    # Canonical
    has_canonical: bool
    canonical_url: str | None

    # Robots
    robots_meta: dict[str, bool] | None

    # Language
    language: str | None

    # Final Score
    seo_score: int

    # NEW
    passed_checks: list[str] = field(default_factory=list)
    failed_checks: list[str] = field(default_factory=list)