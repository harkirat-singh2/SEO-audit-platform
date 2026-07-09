from pydantic import BaseModel


class SEOAnalysisResponse(BaseModel):

    title: str | None
    title_length: int

    meta_description: str | None
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

    seo_score: int

    model_config = {
        "from_attributes": True,
    }