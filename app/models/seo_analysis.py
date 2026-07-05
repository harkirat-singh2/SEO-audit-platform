from datetime import datetime

from sqlalchemy import (
    Boolean,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class SEOAnalysis(Base):
    __tablename__ = "seo_analysis"

    id: Mapped[int] = mapped_column(primary_key=True)

    page_id: Mapped[int] = mapped_column(
        ForeignKey("pages.id"),
        unique=True,
        nullable=False,
    )

    title: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    meta_description: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    h1: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    canonical_url: Mapped[str | None] = mapped_column(
        String(2048),
        nullable=True,
    )

    robots_meta: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    structured_data: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    broken_links: Mapped[int] = mapped_column(
        Integer,
        default=0, 
        nullable=False,
    )

    heading_structure_score: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    image_alt_count: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    word_count: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    readability_score: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    duplicate_content: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    internal_links: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    seo_score: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    analyzed_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    page = relationship(
        "Page",
        back_populates="seo_analysis",
    )