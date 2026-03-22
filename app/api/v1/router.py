from fastapi import APIRouter

from app.api.v1.endpoints import health

api_v1_router = APIRouter()

# ── Register endpoint routers here ──────────────────────────────────────
api_v1_router.include_router(health.router, prefix="/health", tags=["Health"])

# Example — when you add more endpoints:
# from app.api.v1.endpoints import datasets
# api_v1_router.include_router(datasets.router, prefix="/datasets", tags=["Datasets"])
