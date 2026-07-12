from app.response_schemas.audit import AuditDashboard
from app.schemas import AuditResult
from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Response,
    status,
)
from sqlalchemy.orm import Session, joinedload
from app.api.deps import get_db
from app.models.audit import Audit
from app.models.page import Page  # Correct location # Ensure Page model is imported for options
from app.schemas import (
    AuditDetail,
    AuditRequest,
    AuditResponse,
    AuditSummary,
)
from app.services.audit_service import AuditService
from sqlalchemy.orm import joinedload
from app.models.page import Page
from app.response_schemas import AuditDetailResponse
from fastapi.responses import FileResponse
from app.services.pdf_service import PDFService

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
    response_model=list[AuditDashboard],
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
    response_model=AuditDetailResponse,
)
def get_audit(
    audit_id: int,
    db: Session = Depends(get_db),
):
    """
    Return a single audit with pages, SEO analysis, and AI recommendations.
    """
    audit = (
        db.query(Audit)
        .options(
            joinedload(Audit.pages).joinedload(Page.seo_analysis),
            joinedload(Audit.pages).joinedload(Page.recommendation),
        )
        .filter(Audit.id == audit_id)
        .first()
    )
    if audit is None:
        raise HTTPException(
            status_code=404,
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


@router.get("/{audit_id}/report")
def download_report(
    audit_id: int,
    db: Session = Depends(get_db),
):
    print("=" * 50)
    print("PDF REQUESTED")
    print("Audit ID:", audit_id)

    audit = (
        db.query(Audit)
        .options(
            joinedload(Audit.pages)
            .joinedload(Page.seo_analysis),
            joinedload(Audit.pages)
            .joinedload(Page.recommendation),
        )
        .filter(Audit.id == audit_id)
        .first()
    )
    if audit is None:
        raise HTTPException(
            status_code=404,
            detail="Audit not found",
        )
    if not audit.pages:
        raise HTTPException(
            status_code=404,
            detail="No pages found for this audit",
        )

    print("Website:", audit.website_url)
    print("Page:", audit.pages[0].url)
    print("Score:", audit.pages[0].seo_analysis.seo_score)

    result = AuditResult(
        page=audit.pages[0],
        seo=audit.pages[0].seo_analysis,
        recommendation=audit.pages[0].recommendation,
    )
    pdf_service = PDFService()
    filename = f"audit_{audit.id}.pdf"

    print("Generating:", filename)

    pdf_service.generate(
        result=result,
        filename=filename,
    )
    return FileResponse(
        filename,
        media_type="application/pdf",
        filename=filename,
    )
