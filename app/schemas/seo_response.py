from pydantic import BaseModel


class SEOResponse(BaseModel):
    seo_score: int

    title: str | None
    meta_description: str | None

    title_length: int
    meta_description_length: int

    word_count: int

    h1_count: int
    h2_count: int
    total_headings: int

    total_images: int
    images_without_alt: int

    internal_links: int
    external_links: int

    has_canonical: bool
    canonical_url: str | None

    language: str | None

    model_config = {
        "from_attributes": True
    }