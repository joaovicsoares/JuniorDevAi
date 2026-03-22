from app.core.config import settings
from app.schemas.health import HealthResponse


class HealthService:
    """
    Business-logic layer for the health endpoint.

    In a real service this could check database connectivity,
    cache status, downstream AI service reachability, etc.
    """

    def check(self) -> HealthResponse:
        return HealthResponse(
            status="healthy",
            version=settings.APP_VERSION,
        )
