from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Response,
    status,
)
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.models.audit import Audit
from app.schemas import (
    AuditDetail,
    AuditRequest,
    AuditResponse,
    AuditSummary,
)
from app.services.audit_service import AuditService

router = APIRouter()


@router.post(
    "/",
    response_model=AuditResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_audit(
    request: AuditRequest,
    db: Session = Depends(get_db),
):
    """
    Run an SEO audit.
    """
    service = AuditService(db)
    audit = service.run_audit(
        url=str(request.url),
        max_pages=request.max_pages,
    )
    audit_id = audit["audit_id"]
    return AuditResponse(
        message="Audit completed successfully",
        audit_id=audit_id,
    )


@router.get(
    "/",
    response_model=list[AuditSummary],
)
def get_audits(
    db: Session = Depends(get_db),
):
    """
    Return all audits.
    """
    audits = (
        db.query(Audit)
        .order_by(Audit.started_at.desc())
        .all()
    )
    return audits


@router.get(
    "/{audit_id}",
    response_model=AuditDetail,
)
def get_audit(
    audit_id: int,
    db: Session = Depends(get_db),
):
    """
    Return a single audit.
    """
    audit = (
        db.query(Audit)
        .filter(Audit.id == audit_id)
        .first()
    )
    if audit is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Audit not found",
        )
    return audit


@router.delete(
    "/{audit_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_audit(
    audit_id: int,
    db: Session = Depends(get_db),
):
    """
    Delete an audit.
    """
    audit = (
        db.query(Audit)
        .filter(Audit.id == audit_id)
        .first()
    )
    if audit is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Audit not found",
        )
    db.delete(audit)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
