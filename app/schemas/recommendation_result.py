from dataclasses import dataclass


@dataclass
class RecommendationResult:
    """
    AI-generated SEO recommendations.
    """

    meta_title: str

    meta_description: str

    heading_structure: str

    image_alt_text_recommendation: str

    link_recommendation: str

    page_speed_suggestion: str

    mobile_optimization_suggestion: str

    crawl_delay_suggestion: str