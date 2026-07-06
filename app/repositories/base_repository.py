from sqlalchemy.orm import Session


class BaseRepository:
    """
    Base repository providing access to the database session.
    """

    def __init__(
        self,
        db: Session,
    ):
        self.db = db