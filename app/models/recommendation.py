from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Recommendation(Base):
    __tablename__ = "recommendations"

    id: Mapped[int] = mapped_column(primary_key=True)

    page_id: Mapped[int] = mapped_column(
        ForeignKey("pages.id"),
        unique=True,
        nullable=False,
    )

    seo_issues: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    improvement_suggestions: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    suggested_title: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    suggested_meta_description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    content_recommendations: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    page = relationship(
        "Page",
        back_populates="recommendation",
    )