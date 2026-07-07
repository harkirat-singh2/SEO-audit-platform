from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String, Text
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

    meta_title: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    meta_description: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    heading_structure: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    image_alt_text_recommendation: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    link_recommendation: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    page_speed_suggestion: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    mobile_optimization_suggestion: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    crawl_delay_suggestion: Mapped[str | None] = mapped_column(
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