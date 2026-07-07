from dataclasses import dataclass

from app.schemas import (
    PageData,
    RecommendationResult,
    SEOResult,
)


@dataclass
class AuditResult:
    """
    Represents the complete result for a single audited page.
    """

    page: PageData
    seo: SEOResult
    recommendation: RecommendationResult | None