from sqlalchemy.orm import Session
from app.core.config import settings
from app.core.logger import logger
from app.crawler.crawler import WebsiteCrawler
from app.services.seo_analyzer import SEOAnalyzer
from app.services.recommendation_service import RecommendationService
from app.schemas import AuditResult


class AuditService:
    """
    Coordinates the complete SEO audit workflow.
    """

    def __init__(
        self,
        db: Session,
    ):
        self.db = db

        self.analyzer = SEOAnalyzer()
        self.recommendation_service = RecommendationService()

    def run_audit(
    self,
    url: str,
):
        """
        Crawl a website, analyze each page, and generate AI recommendations.
        """

        logger.info("Starting audit for %s", url)

        crawler = WebsiteCrawler(
            base_url=url,
        )

        pages = crawler.crawl()

        logger.info("Crawled %d pages", len(pages))

        results = []

        for index, page in enumerate(pages):

            logger.info("Analyzing page: %s", page.url)

            seo_result = self.analyzer.analyze(page)

            recommendation = None

            if index < settings.MAX_AI_RECOMMENDATIONS:
                logger.info("Generating AI recommendations")

                recommendation = self.recommendation_service.generate(
                    seo_result,
                )
            else:
                logger.info(
                    "Skipping AI recommendation for %s (limit reached)",
                    page.url,
                )

            results.append(
            AuditResult(
                page=page,
                seo=seo_result,
                recommendation=recommendation,
            )
        )

        logger.info("Audit completed successfully")

        return results