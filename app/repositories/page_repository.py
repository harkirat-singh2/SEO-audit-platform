from app.models.page import Page
from app.repositories.base_repository import BaseRepository


class PageRepository(BaseRepository):
    """
    Handles database operations for pages.
    """

    def create(
        self,
        page: Page,
    ) -> Page:

        self.db.add(page)
        self.db.commit()
        self.db.refresh(page)

        return page

    def get_by_audit(
        self,
        audit_id: int,
    ) -> list[Page]:

        return (
            self.db.query(Page)
            .filter(Page.audit_id == audit_id)
            .all()
        )