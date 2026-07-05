from datetime import datetime
from enum import Enum as PyEnum

from sqlalchemy import DateTime, Enum, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base
from app.enums.audit_status import AuditStatus


class Audit(Base):
  __tablename__ = "audits"
  id: Mapped[int] = mapped_column(primary_key=True)
  website_url: Mapped[str] = mapped_column(
    String(2048),
    nullable=False,
)
  status: Mapped[AuditStatus] = mapped_column(
    Enum(AuditStatus),
    default=AuditStatus.PENDING,
    nullable=False,
)
  started_at: Mapped[datetime] = mapped_column( #Why datetime.utcnow and not datetime.utcnow()?
    DateTime,
    default=datetime.utcnow,
    nullable=False,
)
  completed_at: Mapped[datetime | None] = mapped_column(
    DateTime,
    nullable=True,
)
  error_message: Mapped[str | None] = mapped_column(
    Text,
    nullable=True,
)

  pages = relationship(
    "Page",
    back_populates="audit",
    cascade="all, delete-orphan",
)