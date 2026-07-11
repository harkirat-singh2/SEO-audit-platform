from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    """
    Base class for all SQLAlchemy ORM models.
    """
    pass
from app.models.audit import Audit
from app.models.page import Page