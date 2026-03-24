from fastapi import APIRouter

from app.api.v1.endpoints import health, repositories

api_v1_router = APIRouter()

# ── Register endpoint routers here ──────────────────────────────────────
api_v1_router.include_router(health.router, prefix="/health", tags=["Health"])
api_v1_router.include_router(
    repositories.router,
    prefix="/repositories",
    tags=["Repositories"],
)

# Example — when you add more endpoints:
# from app.api.v1.endpoints import datasets
# api_v1_router.include_router(datasets.router, prefix="/datasets", tags=["Datasets"])
