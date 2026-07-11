from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.router import router
from app.database.base import Base
from app.database.session import engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create all database tables if they don't exist
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title="AI SEO Audit Platform",
    version="1.0.0",
    description="AI-powered Website SEO Audit Platform",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://seo-audit-platform-qr3ba7tk7-harkiratemails-7727s-projects.vercel.app",
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


@app.get("/")
def root():
    return {
        "message": "AI SEO Audit Platform",
    }