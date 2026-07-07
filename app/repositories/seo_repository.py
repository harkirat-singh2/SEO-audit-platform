from sqlalchemy.orm import Session

from app.models.seo_analysis import SEOAnalysis


class SEORepository:

    def __init__(self, db: Session):
        self.db = db

    def create(
        self,
        analysis: SEOAnalysis,
    ) -> SEOAnalysis:

        self.db.add(analysis)
        self.db.flush()

        return analysis