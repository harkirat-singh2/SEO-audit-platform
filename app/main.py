from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.health import router
from app.core.config import settings
from app.database.init_db import init_db
from app.core.logger import logger

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Initializing database...")
    init_db()
    logger.info("Database initialized successfully.")
    yield


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    lifespan=lifespan,
)

app.include_router(router)