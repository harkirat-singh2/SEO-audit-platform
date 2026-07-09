from datetime import datetime

from pydantic import BaseModel

from app.response_schemas.seo_analysis import SEOAnalysisResponse
from app.response_schemas.recommendation import RecommendationResponse


class PageResponse(BaseModel):

    id: int

    url: str

    http_status: int

    crawled_at: datetime

    seo_analysis: SEOAnalysisResponse | None

    recommendation: RecommendationResponse | None

    model_config = {
        "from_attributes": True,
    }