from fastapi import FastAPI

from app.api.router import router

app = FastAPI(
    title="AI SEO Audit Platform",
    version="1.0.0",
    description="AI-powered Website SEO Audit Platform",
)

app.include_router(router)


@app.get("/")
def root():
    return {
        "message": "AI SEO Audit Platform",
    }