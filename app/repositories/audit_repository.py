from sqlalchemy.orm import Session

from app.models.audit import Audit


class AuditRepository:
    """
    Handles database operations for audits.
    """

    def __init__(self, db: Session):
        self.db = db

    def create(self, audit: Audit) -> Audit:
        self.db.add(audit)
        self.db.flush()
        return audit

    def get(self, audit_id: int) -> Audit | None:
        return (
            self.db.query(Audit)
            .filter(Audit.id == audit_id)
            .first()
        )

    def get_all(self) -> list[Audit]:
        return (
            self.db.query(Audit)
            .order_by(Audit.started_at.desc())
            .all()
        )

    def delete(self, audit: Audit) -> None:
        self.db.delete(audit)

    def commit(self) -> None:
        self.db.commit()

    def rollback(self) -> None:
        self.db.rollback()