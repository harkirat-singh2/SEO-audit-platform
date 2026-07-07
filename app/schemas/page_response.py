from datetime import datetime

from pydantic import BaseModel


class PageResponse(BaseModel):
    id: int
    url: str
    http_status: int
    crawled_at: datetime

    model_config = {
        "from_attributes": True
    }