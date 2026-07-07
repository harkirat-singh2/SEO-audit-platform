from app.database.base import Base
from app.database.session import engine

# Import all models so SQLAlchemy knows about them
from app.models.audit import Audit
from app.models.page import Page
from app.models.seo_analysis import SEOAnalysis
from app.models.recommendation import Recommendation

Base.metadata.create_all(bind=engine)

print("Database tables created successfully!")