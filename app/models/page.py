from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Page(Base):
    __tablename__ = "pages"

    id: Mapped[int] = mapped_column(primary_key=True)

    audit_id: Mapped[int] = mapped_column(
        ForeignKey("audits.id"),
        nullable=False,
    )

    url: Mapped[str] = mapped_column(
        String(2048),
        nullable=False,
    )

    http_status: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    crawled_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    audit = relationship(
    "Audit",
    back_populates="pages",
)

    seo_analysis = relationship(
        "SEOAnalysis",
        back_populates="page",
        uselist=False,
        cascade="all, delete-orphan",
    )

    recommendation = relationship(
        "Recommendation",
        back_populates="page",
        uselist=False,  # because one page has exactly one SEO analysis and one recommendation.
        cascade="all, delete-orphan",  # if page is deleted, its recommendation will also be deleted.
    )