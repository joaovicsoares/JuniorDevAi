"""
Health-check endpoint — reference example.

This file demonstrates the full pattern:
  Endpoint (router) → Service → Schema
"""

from fastapi import APIRouter, Depends

from app.schemas.health import HealthResponse
from app.services.health_service import HealthService

router = APIRouter()


def get_health_service() -> HealthService:
    """Dependency injector for HealthService."""
    return HealthService()


@router.get(
    "/",
    response_model=HealthResponse,
    summary="Service health check",
    description="Returns the current status and version of the API.",
)
async def health_check(
    service: HealthService = Depends(get_health_service),
) -> HealthResponse:
    return service.check()
