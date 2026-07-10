from fastapi import FastAPI

from app.routers.upload import router as upload_router
from app.routers.query import router as query_router


app = FastAPI(
    title="Intelligent Document Query System",
    description="AI-powered REST API for semantic document search and question answering.",
    version="1.0.0"
)


# Register Routers
app.include_router(upload_router)
app.include_router(query_router)


@app.get("/")
def home():
    return {
        "project": "Intelligent Document Query System",
        "status": "Running",
        "version": "1.0.0"
    }


@app.get("/health")
def health():
    return {
        "status": "Healthy"
    }