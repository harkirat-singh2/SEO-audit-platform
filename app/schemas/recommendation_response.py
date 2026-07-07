from pydantic import BaseModel


class RecommendationResponse(BaseModel):
    meta_title: str | None
    meta_description: str | None
    heading_structure: str | None
    image_alt_text_recommendation: str | None
    link_recommendation: str | None
    page_speed_suggestion: str | None
    mobile_optimization_suggestion: str | None
    crawl_delay_suggestion: str | None

    model_config = {
        "from_attributes": True
    }