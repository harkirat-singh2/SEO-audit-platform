from fastapi import APIRouter

from app.api.routes.audit import router as audit_router
from app.api.routes.health import router as health_router

router = APIRouter()

router.include_router(
    health_router,
    tags=["Health"],
)

router.include_router(
    audit_router,
    prefix="/audits",
    tags=["Audits"],
)