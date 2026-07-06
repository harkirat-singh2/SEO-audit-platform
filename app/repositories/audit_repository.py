from app.models.audit import Audit
from app.repositories.base_repository import BaseRepository


class AuditRepository(BaseRepository):
    """
    Handles database operations for audits.
    """

    def create(
        self,
        audit: Audit,
    ) -> Audit:

        self.db.add(audit)
        self.db.commit()
        self.db.refresh(audit)

        return audit

    def update(
        self,
        audit: Audit,
    ) -> Audit:

        self.db.commit()
        self.db.refresh(audit)

        return audit

    def get_by_id(
        self,
        audit_id: int,
    ) -> Audit | None:

        return (
            self.db.query(Audit)
            .filter(Audit.id == audit_id)
            .first()
        )