from pydantic import BaseModel


class AuditResponse(BaseModel):
    message: str
    audit_id: int