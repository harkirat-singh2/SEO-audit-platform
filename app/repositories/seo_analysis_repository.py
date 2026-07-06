from app.models import SEOAnalysis
from app.repositories.base_repository import BaseRepository

class SEOAnalysisRepository(BaseRepository):

    def create(
        self,
        analysis: SEOAnalysis,
    ) -> SEOAnalysis:

        self.db.add(analysis)
        self.db.commit()
        self.db.refresh(analysis)

        return analysis