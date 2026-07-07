from pydantic import BaseModel, HttpUrl


class AuditRequest(BaseModel):
    url: HttpUrl
    max_pages: int = 5