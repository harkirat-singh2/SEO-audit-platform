from sqlalchemy.orm import Session

from app.models.page import Page


class PageRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, page: Page) -> Page:
        self.db.add(page)
        self.db.flush()
        return page