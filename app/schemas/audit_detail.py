from pydantic import BaseModel

from app.schemas.page_response import PageResponse


class AuditDetail(BaseModel):
    id: int
    website_url: str
    status: str

    pages: list[PageResponse]

    model_config = {
        "from_attributes": True
    }