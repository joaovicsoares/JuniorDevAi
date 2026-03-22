import time
import logging

from fastapi import FastAPI, Request

logger = logging.getLogger(__name__)


async def log_requests(request: Request, call_next):
    """Logs every request with its processing time."""
    start = time.perf_counter()
    response = await call_next(request)
    elapsed_ms = (time.perf_counter() - start) * 1_000

    logger.info(
        "%s %s → %s (%.1f ms)",
        request.method,
        request.url.path,
        response.status_code,
        elapsed_ms,
    )
    return response


def register_middleware(app: FastAPI) -> None:
    """Register all custom middleware on the app instance."""
    app.middleware("http")(log_requests)
