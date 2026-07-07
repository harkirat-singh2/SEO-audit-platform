from datetime import datetime

from pydantic import BaseModel


class AuditSummary(BaseModel):
    id: int
    website_url: str
    status: str
    started_at: datetime
    completed_at: datetime | None

    model_config = {
        "from_attributes": True
    }