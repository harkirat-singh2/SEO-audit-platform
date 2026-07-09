from datetime import datetime
from pydantic import BaseModel

from app.response_schemas.page import PageResponse


class AuditDashboard(BaseModel):
    id: int
    website_url: str
    status: str
    started_at: datetime
    completed_at: datetime | None
    pages: list[PageResponse]

    model_config = {
        "from_attributes": True,
    }


class AuditDetailResponse(BaseModel):
    id: int
    website_url: str
    status: str
    started_at: datetime
    completed_at: datetime | None
    pages: list[PageResponse]

    model_config = {
        "from_attributes": True,
    }