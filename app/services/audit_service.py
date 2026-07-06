import logging
from app.database import 
logger = logging.getLogger(__name__)


class AuditService:

    def __init__(
        self,
        db: Session,
    ):
        self.db = db

        self.crawler = WebsiteCrawler

        self.analyzer = SEOAnalyzer()

        self.recommendation_service = RecommendationService()

        self.pdf_generator = PDFGenerator()