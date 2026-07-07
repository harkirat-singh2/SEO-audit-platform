from datetime import datetime

from sqlalchemy import (
    Boolean,
    DateTime,
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

    # Title
    title: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    title_length: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    # Meta Description
    meta_description: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    meta_description_length: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    # Content
    word_count: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    # Headings
    h1_count: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    h2_count: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    total_headings: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    # Images
    total_images: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    images_without_alt: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    # Links
    internal_links: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    external_links: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    # Canonical
    has_canonical: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    canonical_url: Mapped[str | None] = mapped_column(
        String(2048),
        nullable=True,
    )

    # Robots
    robots_meta: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    # Language
    language: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
    )

    # Final Score
    seo_score: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
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