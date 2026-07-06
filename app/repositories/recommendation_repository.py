from app.models import Recommendation
from app.repositories.base_repository import BaseRepository


class RecommendationRepository(BaseRepository):

    def create(
        self,
        recommendation: Recommendation,
    ) -> Recommendation:

        self.db.add(recommendation)
        self.db.commit()
        self.db.refresh(recommendation)

        return recommendation