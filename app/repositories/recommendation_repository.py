from sqlalchemy.orm import Session

from app.models.recommendation import Recommendation


class RecommendationRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(
        self,
        recommendation: Recommendation,
    ) -> Recommendation:

        self.db.add(recommendation)
        self.db.flush()

        return recommendation